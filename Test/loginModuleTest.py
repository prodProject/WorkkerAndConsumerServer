from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.loginModuleService import LoginModuleService
from Services.loginService import LoginService
from protobuff.login_pb2 import LoginRequestPb

m_login = LoginModuleService()
m_loginService = LoginService()
m_loginReq = LoginRequestPb()
m_loginReq.login.CopyFrom(m_loginService.get(id="kZ"))
m_converter = ConvertJSONToPb()
print(m_login.login(loginRequestPb=m_loginReq))
