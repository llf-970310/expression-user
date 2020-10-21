import logging

import mongoengine
from config import MongoConfig
from user import UserService
from user.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import handler


class UserServiceHandler:
    def __init__(self):
        self.log = {}

    def authenticate(self, request: AuthenticateRequest) -> AuthenticateResponse:
        return handler.verify_user(request)

    def authenticateWechatUser(self, request: AuthenticateWechatUserRequest) -> AuthenticateWechatUserResponse:
        return handler.verify_wechat_user(request)

    def createUser(self, request: CreateUserRequest) -> CreateUserResponse:
        return handler.create_user(request)

    def checkExamPermission(self, request: CheckExamPermissionRequest) -> CheckExamPermissionResponse:
        return handler.check_exam_permission(request)

    def getUserInfo(self, request: GetUserInfoRequest) -> GetUserInfoResponse:
        return handler.get_user_info(request)

    def updateUserInfo(self, request: UpdateUserInfoRequest) -> UpdateUserInfoResponse:
        return handler.update_user_info(request)

    def getInvitationCode(self, request: GetInvitationCodeRequest) -> GetInvitationCodeResponse:
        return handler.get_invitation_code(request)

    def createInvitationCode(self, request: CreateInvitationCodeRequest) -> CreateInvitationCodeResponse:
        return handler.create_invitation_code(request)


if __name__ == '__main__':
    # init mongo
    mongoengine.connect(
        db=MongoConfig.db,
        host=MongoConfig.host,
        port=MongoConfig.port,
        username=MongoConfig.user,
        password=MongoConfig.password
    )

    # init logging
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    # init thrift server
    exam_handler = UserServiceHandler()
    processor = UserService.Processor(exam_handler)
    transport = TSocket.TServerSocket(host='127.0.0.1', port=9092)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    # You could do one of these for a multithreaded server
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    server.serve()
