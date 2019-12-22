from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.sendPushNotificationService import SendPushNotificationService
from protobuff import pushnotification_pb2


class SendPushNotificationHandler:

    @staticmethod
    def snedNotification(builder):
        service = SendPushNotificationService()
        m_converter = ConvertJSONToPb()
        m_convertPbtoJson = ConvertPbToJSON()
        builder = m_converter.converjsontoPBProper(response=builder,
                                                   instanceType=pushnotification_pb2.PushNotificationRequestPb())
        return m_convertPbtoJson.converPbtojson(service.sendNotification(pushNotificationRequestPb=builder))
