import datetime
import logging
import traceback

import util
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


def check_exam_permission(user_id: str):
    user = UserModel.objects(id=user_id).first()
    if user.remaining_exam_num <= 0:
        raise NoExamTimes
    now = datetime.datetime.utcnow()
    if user.vip_end_time <= now:
        raise VipExpired


def get_user_info(user_id: str) -> UserInfo:
    user = UserModel.objects(id=user_id).first()
    if not user:
        raise UserNotExist

    return UserInfo(
        role=str(user.role.value),
        nickName=user.name,
        email=user.email,
        phone=user.phone,
        wechatId=user.wx_id,
        remainingExamNum=user.remaining_exam_num,
        registerTime=util.datetime_to_str(user.register_time),
        lastLoginTime=util.datetime_to_str(user.last_login_time),
        vipStartTime=util.datetime_to_str(user.vip_start_time),
        vipEndTime=util.datetime_to_str(user.vip_end_time),
        questionHistory=[key for key, val in user.questions_history.items()],
    )


def update_user_info(user_id: str, invitation_code: str):
    user = UserModel.objects(id=user_id).first()
    if not user:
        raise UserNotExist

    existing_invitation = InvitationModel.objects(code=invitation_code).first()
    if existing_invitation is None or existing_invitation.available_times <= 0:
        raise InvalidInvitationCode

    logging.info(
        '[update_user_info][update_privilege] email:%s, phone:%s, code:%s' % (user.email, user.phone, invitation_code))

    # todo: 开始同步，修改邀请码及用户信息
    existing_invitation.activate_users.append(user.email if user.email else user.phone)
    if existing_invitation.available_times <= 0:
        raise InvalidInvitationCode
    existing_invitation.available_times -= 1
    existing_invitation.save()
    user.vip_start_time = existing_invitation.vip_start_time
    user.vip_end_time = existing_invitation.vip_end_time
    user.remaining_exam_num = existing_invitation.remaining_exam_num
    user.invitation_code = existing_invitation.code
    user.save()
    # todo: 同步结束


def get_invitation_code(code, create_time_from, create_time_to, available_times, page, page_size) -> (list, int):
    try:
        n_from = page_size * (page - 1)
        d = {}
        time_limits = {}
        if create_time_from:
            time_limits.update({'$gte': util.datetime_fromisoformat(create_time_from)})
        if create_time_to:
            time_limits.update({'$lte': util.datetime_fromisoformat(create_time_to)})
        if time_limits != {}:
            d.update({'create_time': time_limits})
        if available_times not in [None, '']:
            d.update({'available_times': int(available_times)})
        if code:
            d.update({'code': code})
    except Exception as e:
        traceback.print_exc()
        raise InvalidParam

    set_manager = InvitationModel.objects(__raw__=d)
    invitations = set_manager.skip(n_from).limit(page_size)
    total = set_manager.count()

    result = []
    for invitation in invitations:
        result.append(InvitationCode(
            code=invitation['code'],
            creator=invitation['creator'],
            createTime=util.datetime_to_str(invitation['create_time']),
            availableTimes=invitation['available_times'],
            vipStartTime=util.datetime_to_str(invitation['vip_start_time']),
            vipEndTime=util.datetime_to_str(invitation['vip_end_time']),
            remainingExamNum=invitation['remaining_exam_num'],
            remainingExerciseNum=invitation['remaining_exercise_num'],
            activateUsers=invitation['activate_users'],
        ))

    return result, total
