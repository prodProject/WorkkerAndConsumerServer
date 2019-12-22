from Services.pushNotificationService import PushNotificationService
from protobuff.persontypeenum_pb2 import WORKER
from protobuff.pushnotification_pb2 import PushNotificationPb, PushNotificationSearchRequestPb

m_service = PushNotificationService()

m_builder = PushNotificationSearchRequestPb();
m_builder.workerRef.dbInfo.id= '96'
m_builder.type.personType = WORKER

print(m_service.search(builder=m_builder))
