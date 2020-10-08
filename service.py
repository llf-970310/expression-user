import datetime
import logging

from config import SystemConfig
from errors import *
from manager import token_manager, wx_platform_manager
from model.user import UserModel
from user.ttypes import *
from util import validate_email, validate_phone


def create_user(name: str, wx_id: str) -> UserModel:
    new_user = UserModel()
    new_user.name = name
    new_user.wx_id = wx_id
    new_user.last_login_time = datetime.datetime.utcnow()
    new_user.register_time = datetime.datetime.utcnow()
    new_user.save()

    return new_user


def verify_user(username: str, password: str) -> str:
    # 邮箱登录
    if '@' in username:
        if not validate_email(username):
            raise InvalidParam
        check_user = UserModel.objects(email=username).first()
    # 手机号登录
    else:
        if not validate_phone(username):
            raise InvalidParam
        check_user = UserModel.objects(phone=username).first()

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
        check_user = create_user(name=nick_name, wx_id=openid)

    token = token_manager.generate_token(check_user)
    check_user.update(last_login_time=datetime.datetime.utcnow())
    logging.info('verify wechat user successful. nick_name=%s, user_id=%s' % (check_user.name, check_user.id))

    return token
