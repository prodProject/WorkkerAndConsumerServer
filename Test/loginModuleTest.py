from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.loginModuleService import LoginModuleService
from protobuff.login_pb2 import LoginRequestPb
from protobuff.persontypeenum_pb2 import WORKER

m_loginService = LoginModuleService()
m_loginReq = LoginRequestPb()
m_loginReq.login.contactDetails.email.localPart = "shub";
m_loginReq.login.contactDetails.email.domain = "gmail.com";
m_loginReq.login.password = "qwerty";
m_loginReq.login.personType.personType = WORKER;
m_converter = ConvertJSONToPb()
print(m_loginService.login(loginRequestPb=m_loginReq))
