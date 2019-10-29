from CommonCode.convertJSONTOPb import ConvertJSONToPb
from LoginModule.loginControlFlow import Login
from Services.loginService import LoginService

m_login = Login()
m_loginService = LoginService()
m_converter = ConvertJSONToPb()
m_login.start(loginReq=m_loginService.get(id="kZ"))
print(m_login.done())
