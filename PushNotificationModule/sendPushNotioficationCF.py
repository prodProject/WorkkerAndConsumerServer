from enum import Enum

from PushNotification.pushNotificationModuleService import PushNotificationModule
from PushNotificationModule.sendPushNotificationHelper import SendPushNotificationHelper
from Services.pushNotificationService import PushNotificationService
from protobuff.pushnotification_pb2 import SINGLE, MULTIPLE


class States(Enum):
    START = 0,
    GET_PUSH_NOTIFICATION_TOKEN = 1
    SEND_NOTIFICATION = 2
    DONE = 3,


class SendPushNotification:
    m_helper = SendPushNotificationHelper()
    m_pushNotificationService = PushNotificationService()
    m_sendNotificationModule = PushNotificationModule()
    m_response = None
    m_pushNotificationRequestPb = None

    def start(self, pushNotificationRequestPb):
        self.m_pushNotificationRequestPb = pushNotificationRequestPb
        self.controlFlow(currentState=States.GET_PUSH_NOTIFICATION_TOKEN)

    def done(self):
        return self.m_response

    def getPushNotificationToken(self):
        searchResponse = self.m_pushNotificationService.search(builder=self.m_helper.getPushNotificationSearchRequest(
            pushNotificationRequestPb=self.m_pushNotificationRequestPb))
        if (searchResponse != None):
            self.m_response = searchResponse.results
            self.controlFlow(currentState=States.SEND_NOTIFICATION)
        else:
            self.controlFlow(currentState=States.DONE)

    def sendNotification(self):
        pushNotifiactionBuilder = self.m_helper.getPushNotificationBuilder(searchResponse=self.m_response)
        if (pushNotifiactionBuilder.sendType == SINGLE):
            self.m_response = self.m_sendNotificationModule.sendPushNotificationToSingleDevice(
                pushNptificationBuilderPb=pushNotifiactionBuilder)
            self.controlFlow(currentState=States.DONE)
        elif (pushNotifiactionBuilder.sendType == MULTIPLE):
            self.m_response =self.m_sendNotificationModule.sendPushNotificationToMultipleDevice(
                pushNptificationBuilderPb=pushNotifiactionBuilder)
            self.controlFlow(currentState=States.DONE)
        else:
            self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_PUSH_NOTIFICATION_TOKEN):
            self.getPushNotificationToken()
        elif (currentState == States.SEND_NOTIFICATION):
            self.sendNotification()
        elif (currentState == States.DONE):
            self.done()
