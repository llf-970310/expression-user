import time
import jwt

from model.user import UserModel


def generate_token(user: UserModel) -> str:
    payload = {
        "uuid": str(user.id),
        "nick_name": user.name,
        "role": user.role.value,
        "exp": int(time.time()) + 3600
    }
    token = jwt.encode(payload, "secret", algorithm="HS256")
    return token.decode("utf-8")
