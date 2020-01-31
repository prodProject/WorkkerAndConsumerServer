from Services import sendPushNotificationService
from Services.sendPushNotificationService import SendPushNotificationService
from protobuff.pushnotification_pb2 import PushNotificationRequestPb

service = SendPushNotificationService()
sendNotification = PushNotificationRequestPb()
sendNotification.workerRef.dbInfo.id ="ku"
print(service.sendNotification(pushNotificationRequestPb=sendNotification))


