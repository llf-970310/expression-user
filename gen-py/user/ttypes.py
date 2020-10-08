#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class UserInfo(object):
    """
    Attributes:
     - role
     - nickName
     - email
     - phone
     - wechatId
     - remainingExamNum
     - registerTime
     - lastLoginTime
     - vipStartTime
     - vipEndTime

    """


    def __init__(self, role=None, nickName=None, email=None, phone=None, wechatId=None, remainingExamNum=None, registerTime=None, lastLoginTime=None, vipStartTime=None, vipEndTime=None,):
        self.role = role
        self.nickName = nickName
        self.email = email
        self.phone = phone
        self.wechatId = wechatId
        self.remainingExamNum = remainingExamNum
        self.registerTime = registerTime
        self.lastLoginTime = lastLoginTime
        self.vipStartTime = vipStartTime
        self.vipEndTime = vipEndTime

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.role = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.nickName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.phone = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.wechatId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.remainingExamNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.registerTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.lastLoginTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.vipStartTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.vipEndTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('UserInfo')
        if self.role is not None:
            oprot.writeFieldBegin('role', TType.STRING, 1)
            oprot.writeString(self.role.encode('utf-8') if sys.version_info[0] == 2 else self.role)
            oprot.writeFieldEnd()
        if self.nickName is not None:
            oprot.writeFieldBegin('nickName', TType.STRING, 2)
            oprot.writeString(self.nickName.encode('utf-8') if sys.version_info[0] == 2 else self.nickName)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 3)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.phone is not None:
            oprot.writeFieldBegin('phone', TType.STRING, 4)
            oprot.writeString(self.phone.encode('utf-8') if sys.version_info[0] == 2 else self.phone)
            oprot.writeFieldEnd()
        if self.wechatId is not None:
            oprot.writeFieldBegin('wechatId', TType.STRING, 5)
            oprot.writeString(self.wechatId.encode('utf-8') if sys.version_info[0] == 2 else self.wechatId)
            oprot.writeFieldEnd()
        if self.remainingExamNum is not None:
            oprot.writeFieldBegin('remainingExamNum', TType.I32, 6)
            oprot.writeI32(self.remainingExamNum)
            oprot.writeFieldEnd()
        if self.registerTime is not None:
            oprot.writeFieldBegin('registerTime', TType.I64, 7)
            oprot.writeI64(self.registerTime)
            oprot.writeFieldEnd()
        if self.lastLoginTime is not None:
            oprot.writeFieldBegin('lastLoginTime', TType.I64, 8)
            oprot.writeI64(self.lastLoginTime)
            oprot.writeFieldEnd()
        if self.vipStartTime is not None:
            oprot.writeFieldBegin('vipStartTime', TType.I64, 9)
            oprot.writeI64(self.vipStartTime)
            oprot.writeFieldEnd()
        if self.vipEndTime is not None:
            oprot.writeFieldBegin('vipEndTime', TType.I64, 10)
            oprot.writeI64(self.vipEndTime)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthenticateRequest(object):
    """
    Attributes:
     - username
     - password

    """


    def __init__(self, username=None, password=None,):
        self.username = username
        self.password = password

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthenticateRequest')
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 1)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 2)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.username is None:
            raise TProtocolException(message='Required field username is unset!')
        if self.password is None:
            raise TProtocolException(message='Required field password is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthenticateResponse(object):
    """
    Attributes:
     - token
     - statusCode
     - statusMsg

    """


    def __init__(self, token=None, statusCode=None, statusMsg=None,):
        self.token = token
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthenticateResponse')
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 1)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 2)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 3)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthenticateWechatUserRequest(object):
    """
    Attributes:
     - code
     - nickName

    """


    def __init__(self, code=None, nickName=None,):
        self.code = code
        self.nickName = nickName

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.code = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.nickName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthenticateWechatUserRequest')
        if self.code is not None:
            oprot.writeFieldBegin('code', TType.STRING, 1)
            oprot.writeString(self.code.encode('utf-8') if sys.version_info[0] == 2 else self.code)
            oprot.writeFieldEnd()
        if self.nickName is not None:
            oprot.writeFieldBegin('nickName', TType.STRING, 2)
            oprot.writeString(self.nickName.encode('utf-8') if sys.version_info[0] == 2 else self.nickName)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.code is None:
            raise TProtocolException(message='Required field code is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AuthenticateWechatUserResponse(object):
    """
    Attributes:
     - token
     - statusCode
     - statusMsg

    """


    def __init__(self, token=None, statusCode=None, statusMsg=None,):
        self.token = token
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AuthenticateWechatUserResponse')
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 1)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 2)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 3)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CreateUserRequest(object):
    """
    Attributes:
     - userInfo

    """


    def __init__(self, userInfo=None,):
        self.userInfo = userInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.userInfo = UserInfo()
                    self.userInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('CreateUserRequest')
        if self.userInfo is not None:
            oprot.writeFieldBegin('userInfo', TType.STRUCT, 1)
            self.userInfo.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.userInfo is None:
            raise TProtocolException(message='Required field userInfo is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CreateUserResponse(object):
    """
    Attributes:
     - statusCode
     - statusMsg

    """


    def __init__(self, statusCode=None, statusMsg=None,):
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('CreateUserResponse')
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 1)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 2)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetUserInfoRequest(object):
    """
    Attributes:
     - userId

    """


    def __init__(self, userId=None,):
        self.userId = userId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.userId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('GetUserInfoRequest')
        if self.userId is not None:
            oprot.writeFieldBegin('userId', TType.STRING, 1)
            oprot.writeString(self.userId.encode('utf-8') if sys.version_info[0] == 2 else self.userId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.userId is None:
            raise TProtocolException(message='Required field userId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetUserInfoResponse(object):
    """
    Attributes:
     - userInfo
     - statusCode
     - statusMsg

    """


    def __init__(self, userInfo=None, statusCode=None, statusMsg=None,):
        self.userInfo = userInfo
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.userInfo = UserInfo()
                    self.userInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('GetUserInfoResponse')
        if self.userInfo is not None:
            oprot.writeFieldBegin('userInfo', TType.STRUCT, 1)
            self.userInfo.write(oprot)
            oprot.writeFieldEnd()
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 2)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 3)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.userInfo is None:
            raise TProtocolException(message='Required field userInfo is unset!')
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UpdateUserInfoRequest(object):
    """
    Attributes:
     - userInfo

    """


    def __init__(self, userInfo=None,):
        self.userInfo = userInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.userInfo = UserInfo()
                    self.userInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('UpdateUserInfoRequest')
        if self.userInfo is not None:
            oprot.writeFieldBegin('userInfo', TType.STRUCT, 1)
            self.userInfo.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.userInfo is None:
            raise TProtocolException(message='Required field userInfo is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UpdateUserInfoResponse(object):
    """
    Attributes:
     - statusCode
     - statusMsg

    """


    def __init__(self, statusCode=None, statusMsg=None,):
        self.statusCode = statusCode
        self.statusMsg = statusMsg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.statusCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.statusMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('UpdateUserInfoResponse')
        if self.statusCode is not None:
            oprot.writeFieldBegin('statusCode', TType.I32, 1)
            oprot.writeI32(self.statusCode)
            oprot.writeFieldEnd()
        if self.statusMsg is not None:
            oprot.writeFieldBegin('statusMsg', TType.STRING, 2)
            oprot.writeString(self.statusMsg.encode('utf-8') if sys.version_info[0] == 2 else self.statusMsg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.statusCode is None:
            raise TProtocolException(message='Required field statusCode is unset!')
        if self.statusMsg is None:
            raise TProtocolException(message='Required field statusMsg is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(UserInfo)
UserInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'role', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'nickName', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'email', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'phone', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'wechatId', 'UTF8', None, ),  # 5
    (6, TType.I32, 'remainingExamNum', None, None, ),  # 6
    (7, TType.I64, 'registerTime', None, None, ),  # 7
    (8, TType.I64, 'lastLoginTime', None, None, ),  # 8
    (9, TType.I64, 'vipStartTime', None, None, ),  # 9
    (10, TType.I64, 'vipEndTime', None, None, ),  # 10
)
all_structs.append(AuthenticateRequest)
AuthenticateRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'username', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'password', 'UTF8', None, ),  # 2
)
all_structs.append(AuthenticateResponse)
AuthenticateResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'token', 'UTF8', None, ),  # 1
    (2, TType.I32, 'statusCode', None, None, ),  # 2
    (3, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 3
)
all_structs.append(AuthenticateWechatUserRequest)
AuthenticateWechatUserRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'code', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'nickName', 'UTF8', None, ),  # 2
)
all_structs.append(AuthenticateWechatUserResponse)
AuthenticateWechatUserResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'token', 'UTF8', None, ),  # 1
    (2, TType.I32, 'statusCode', None, None, ),  # 2
    (3, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 3
)
all_structs.append(CreateUserRequest)
CreateUserRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'userInfo', [UserInfo, None], None, ),  # 1
)
all_structs.append(CreateUserResponse)
CreateUserResponse.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'statusCode', None, None, ),  # 1
    (2, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 2
)
all_structs.append(GetUserInfoRequest)
GetUserInfoRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'userId', 'UTF8', None, ),  # 1
)
all_structs.append(GetUserInfoResponse)
GetUserInfoResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'userInfo', [UserInfo, None], None, ),  # 1
    (2, TType.I32, 'statusCode', None, None, ),  # 2
    (3, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 3
)
all_structs.append(UpdateUserInfoRequest)
UpdateUserInfoRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'userInfo', [UserInfo, None], None, ),  # 1
)
all_structs.append(UpdateUserInfoResponse)
UpdateUserInfoResponse.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'statusCode', None, None, ),  # 1
    (2, TType.STRING, 'statusMsg', 'UTF8', None, ),  # 2
)
fix_spec(all_structs)
del all_structs
