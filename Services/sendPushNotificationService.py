from PushNotificationModule.sendPushNotioficationCF import SendPushNotification


class SendPushNotificationService:
    m_sendPushNotification = SendPushNotification()

    def sendNotification(self, pushNotificationRequestPb):
        self.m_sendPushNotification.start(pushNotificationRequestPb=pushNotificationRequestPb)
        return self.m_sendPushNotification.done()
