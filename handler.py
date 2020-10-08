import service

from user.ttypes import *
from errors import *


def verify_user(request: AuthenticateRequest) -> AuthenticateResponse:
    resp = AuthenticateResponse()
    username = request.username.strip().lower()
    password = request.password.strip()

    if username is None or username == "" or password is None or password == "":
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        token = service.verify_user(username, password)
        resp.token = token
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp


def verify_wechat_user(request: AuthenticateWechatUserRequest) -> AuthenticateWechatUserResponse:
    resp = AuthenticateWechatUserResponse()
    code = request.code
    nick_name = request.nickName

    if not code:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        token = service.verify_wechat_user(code, nick_name)
        resp.token = token
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp
