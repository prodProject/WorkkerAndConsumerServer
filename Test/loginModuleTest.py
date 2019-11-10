import bcrypt

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.loginModuleService import LoginModuleService
from protobuff.login_pb2 import LoginRequestPb
from protobuff.persontypeenum_pb2 import WORKER

#'$2b$12$uJFeZ8ZldnTETF6C8tTMteLGrOi0DEsDsQB.xVvZBzZJO5vErm3sa'
m_loginService = LoginModuleService()
m_loginReq = LoginRequestPb()
m_loginReq.login.contactDetails.email.localPart = "d";
m_loginReq.login.contactDetails.email.domain = "c.c";
m_loginReq.login.password = "d";
m_loginReq.login.personType.personType = WORKER;
m_converter = ConvertJSONToPb()
print(m_loginService.login(loginRequestPb=m_loginReq))
