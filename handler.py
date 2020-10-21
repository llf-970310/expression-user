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


def create_user(request: CreateUserRequest) -> CreateUserResponse:
    resp = CreateUserResponse()
    username = request.username.strip().lower()
    password = request.password.strip()
    name = request.name
    invitation_code = request.invitationCode

    if not (username and password and name):
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        service.create_normal_user(username, password, name, invitation_code)
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp


def check_exam_permission(request: CheckExamPermissionRequest) -> CheckExamPermissionResponse:
    resp = CheckExamPermissionResponse()
    user_id = request.userId

    if not user_id:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        service.check_exam_permission(user_id)
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp


def get_user_info(request: GetUserInfoRequest) -> GetUserInfoResponse:
    resp = GetUserInfoResponse()
    user_id = request.userId

    if not user_id:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        user_info = service.get_user_info(user_id)
        resp.userInfo = user_info
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp


def update_user_info(request: UpdateUserInfoRequest) -> UpdateUserInfoResponse:
    resp = UpdateUserInfoResponse()
    user_id = request.userId
    invitation_code = request.invitationCode

    if not user_id:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        service.update_user_info(user_id, invitation_code)
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp


def get_invitation_code(request: GetInvitationCodeRequest) -> GetInvitationCodeResponse:
    resp = GetInvitationCodeResponse()
    code = request.invitationCode
    create_time_from = request.createTimeFrom
    create_time_to = request.createTimeTo
    available_times = request.availableTimes
    page = request.page
    page_size = request.pageSize

    if page < 0 or page_size < 0:
        fill_status_of_resp(resp, InvalidParam())
        return resp

    try:
        code_list, total = service.get_invitation_code(code, create_time_from, create_time_to, available_times, page, page_size)
        resp.invitationCodeList = code_list
        resp.total = total
        fill_status_of_resp(resp)
    except ErrorWithCode as e:
        fill_status_of_resp(resp, e)

    return resp
