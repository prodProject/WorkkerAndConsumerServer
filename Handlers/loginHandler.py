from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.loginModuleService import LoginModuleService
from protobuff.login_pb2 import LoginRequestPb


class LoginHandler:

    @staticmethod
    def getLogin(builder):
        service = LoginModuleService()
        m_converter = ConvertJSONToPb()
        m_convertPbtoJson = ConvertPbToJSON()
        builder = m_converter.converjsontoPBProper(response=builder, instanceType=LoginRequestPb())
        return m_convertPbtoJson.converPbtojson(service.login(loginRequestPb=builder))
