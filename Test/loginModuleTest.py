from CommonCode.convertJSONTOPb import ConvertJSONToPb
from LoginModule.loginControlFlow import Login
from Services.loginModuleService import LoginModuleService
from Services.loginService import LoginService

m_login = LoginModuleService()
m_loginService = LoginService()
m_converter = ConvertJSONToPb()
print(m_login.login(loginRequestPb=m_loginService.get(id="kZ")))
