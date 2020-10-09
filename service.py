import datetime
import logging

from config import SystemConfig
from errors import *
from manager import token_manager, wx_platform_manager, user_manager
from model.invitation import InvitationModel
from model.user import UserModel
from user.ttypes import *
from util import validate_email, validate_phone


def verify_user(username: str, password: str) -> str:
    check_user = user_manager.get_user_by_username(username)

    # 判断该用户是否存在
    if not check_user:
        raise UserNotExist

    # 判断密码是否正确
    if (not SystemConfig.IGNORE_LOGIN_PASSWORD) and (not check_user.check_password(password)):
        raise AuthenticationFailed

    token = token_manager.generate_token(check_user)
    check_user.update(last_login_time=datetime.datetime.utcnow())
    logging.info('verify user successful. nick_name=%s, user_id=%s' % (check_user.name, check_user.id))

    return token


def verify_wechat_user(code: str, nick_name: str) -> str:
    # code -> openid
    err_code, _, openid = wx_platform_manager.get_sessionkey_openid(
        code,
        appid=SystemConfig.WX_APP_APPID,
        secret=SystemConfig.WX_APP_SECRET
    )
    if err_code:
        raise ErrorWithCode(code=int(err_code), msg='获取openid出错')

    # todo: 后续 openid 改存 unionid
    check_user = UserModel.objects(wx_id=openid).first()

    # user not exist -> new
    if not check_user:
        check_user = create_wechat_user(name=nick_name, wx_id=openid)

    token = token_manager.generate_token(check_user)
    check_user.update(last_login_time=datetime.datetime.utcnow())
    logging.info('verify wechat user successful. nick_name=%s, user_id=%s' % (check_user.name, check_user.id))

    return token


def create_wechat_user(name: str, wx_id: str) -> UserModel:
    new_user = UserModel()
    new_user.name = name
    new_user.wx_id = wx_id
    new_user.last_login_time = datetime.datetime.utcnow()
    new_user.register_time = datetime.datetime.utcnow()
    new_user.save()

    return new_user


def create_normal_user(username: str, password: str, name: str, invitation_code: str):
    # 判断用户是否已存在
    exist_user = user_manager.get_user_by_username(username)
    if exist_user:
        raise UserAlreadyExist

    # 基本信息配置
    email, phone = '', ''
    if '@' in username:
        email = username
    else:
        phone = username

    logging.info('[NewUser][register]email:%s, phone:%s' % (email, phone))
    new_user = UserModel()
    new_user.email = email.lower() if email != '' else None
    new_user.phone = phone if phone != '' else None
    new_user.set_password(password)
    new_user.name = name
    new_user.last_login_time = datetime.datetime.utcnow()
    new_user.register_time = datetime.datetime.utcnow()

    # 邀请码相关
    existing_invitation = None
    if invitation_code:
        # 验证邀请码
        existing_invitation = InvitationModel.objects(code=invitation_code).first()
        if existing_invitation is None or existing_invitation.available_times <= 0:
            raise InvalidInvitationCode
        new_user.vip_start_time = existing_invitation.vip_start_time
        new_user.vip_end_time = existing_invitation.vip_end_time
        new_user.remaining_exam_num = existing_invitation.remaining_exam_num
        new_user.invitation_code = existing_invitation.code
    else:
        # 不需要邀请码，使用默认配置
        new_user.vip_start_time = datetime.datetime(2020, 6, 1, 10, 0, 0)
        new_user.vip_end_time = datetime.datetime(2020, 8, 15, 10, 0, 0)
        new_user.remaining_exam_num = 100
        new_user.invitation_code = ""

    # todo: 开始同步，创建用户并修改邀请码信息
    new_user.save()
    if invitation_code:
        # 修改这个邀请码
        existing_invitation.activate_users.append(email if email != '' else phone)
        if existing_invitation.available_times <= 0:
            return InvalidInvitationCode
        existing_invitation.available_times -= 1
        existing_invitation.save()
        logging.info('invitation(id = %s) has been saved' % existing_invitation.id)
    # todo: 同步结束
