from errors import InvalidParam
from model.user import UserModel
from util import validate_email, validate_phone


# 根据 username 找用户，不存在返回 None
def get_user_by_username(username: str) -> UserModel:
    user = None
    # 邮箱登录
    if '@' in username:
        if not validate_email(username):
            raise InvalidParam
        user = UserModel.objects(email=username).first()
    # 手机号登录
    else:
        if not validate_phone(username):
            raise InvalidParam
        user = UserModel.objects(phone=username).first()
    return user
