from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.registrationWorkerService import RegistrationWorkerService
from protobuff import registration_pb2


class RegistrionHandler:

    @staticmethod
    def createRegistrationworker(builder):
        service = RegistrationWorkerService()
        m_converter = ConvertJSONToPb()
        m_convertPbtoJson = ConvertPbToJSON()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=registration_pb2.RegistrationRequestPb())
        return m_convertPbtoJson.converPbtojson(service.registration(registrationRequestPb=builder))
