from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Handlers.loginHandler import LoginHandler
from Services.loginModuleService import LoginModuleService
from protobuff import login_pb2
from protobuff.persontypeenum_pb2 import WORKER

#'$2b$12$uJFeZ8ZldnTETF6C8tTMteLGrOi0DEsDsQB.xVvZBzZJO5vErm3sa'
m_loginService = LoginModuleService()
#m_loginReq = LoginRequestPb()

builder = "{\"login\":{\"contactDetails\":{\"email\":{\"localPart\":\"shubhamtiwaricr07\",\"domain\":\"gmail.com\"}},\"password\":\"nikerisk\",\"personType\":{\"personType\":\"WORKER\"}}}";
m_converter = ConvertJSONToPb()
print(LoginHandler.getLogin(builder=builder))
