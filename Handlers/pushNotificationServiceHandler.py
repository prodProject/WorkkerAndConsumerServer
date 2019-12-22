from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.pushNotificationService import PushNotificationService
from protobuff import pushnotification_pb2


class PushNotificationServiceHandler:

    @staticmethod
    def getPushNotification(id):
        service = PushNotificationService()
        m_convertPbtoJson = ConvertPbToJSON()
        return m_convertPbtoJson.converPbtojson(service.get(id=id))

    @staticmethod
    def createPushNotification(builder):
        service = PushNotificationService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,
                                                   instanceType=pushnotification_pb2.PushNotificationPb())
        return service.create(builder=builder)

    @staticmethod
    def updatePushNotification(builder):
        service = PushNotificationService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,
                                                   instanceType=pushnotification_pb2.PushNotificationRequestPb())
        return service.update(id=builder.dbInfo.id, builder=builder)

    @staticmethod
    def searchPushNotification(builder):
        service = PushNotificationService()
        m_converter = ConvertJSONToPb()
        builder = m_converter.converjsontoPBProper(response=builder,
                                                   instanceType=pushnotification_pb2.PushNotificationSearchRequestPb())
        return service.search(builder=builder)
