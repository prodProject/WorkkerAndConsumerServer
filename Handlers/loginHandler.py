from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.loginModuleService import LoginModuleService
from protobuff import login_pb2

class LoginHandler:

    @staticmethod
    def getLogin(builder):
        service = LoginModuleService()
        m_converter = ConvertJSONToPb()
        m_convertPbtoJson = ConvertPbToJSON()
        builder = m_converter.converjsontoPBProper(response=builder, instanceType=login_pb2.LoginRequestPb())
        print(builder)
        return m_convertPbtoJson.converPbtojson(service.login(loginRequestPb=builder))
