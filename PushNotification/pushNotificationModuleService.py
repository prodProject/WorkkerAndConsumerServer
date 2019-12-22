from pyfcm import FCMNotification


class PushNotificationModule:
    m_api_key = "AAAAltGCeGs:APA91bElD5bksaGH4oLKIvCSPLvzpVZMX3UxuMII1LkOyVzJ_D7xA53XCQt-n4pI1rkRc10VnZuHgJKvHx_M-0yXkI9pIouhZvQHfsRMmrmo3T84y-YTfbTcuez3-lxGBcDBKOBRpMH1"
    push_service = None

    def __init__(self):
        self.push_service = FCMNotification(api_key=self.m_api_key)
        if (self.push_service == None):
            self.__init__()

    def sendPushNotificationToSingleDevice(self, pushNptificationBuilderPb):
        return self.push_service.notify_single_device(registration_id=pushNptificationBuilderPb.registrationId,
                                               message_title=pushNptificationBuilderPb.subject,
                                               message_body=pushNptificationBuilderPb.body)

    def sendPushNotificationToMultipleDevice(self, pushNptificationBuilderPb):
        return self.push_service.notify_single_device(registration_id=pushNptificationBuilderPb.registrationIds,
                                               message_title=pushNptificationBuilderPb.subject,
                                               message_body=pushNptificationBuilderPb.body)
