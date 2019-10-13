from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Services.registrationWorkerService import RegistrationWorkerService
from protobuff import registration_pb2


class RegistrionHandler:

    @staticmethod
    def createRegistrationworker(builder):
        service = RegistrationWorkerService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,instanceType=registration_pb2.RegistrationRequestPb())
        return service.registration(registrationRequestPb=builder)
