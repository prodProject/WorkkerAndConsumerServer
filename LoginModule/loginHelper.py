from protobuff.entity_pb2 import ACTIVE
from protobuff.login_pb2 import LoginSearchRequestPb


class LoginHelper:

    def getLoginSearchReqbuestBuilder(self,loginPb):
        print(loginPb)
        req = LoginSearchRequestPb()
        req.lifeTime = ACTIVE
        req.login.CopyFrom(loginPb)
        return req;
