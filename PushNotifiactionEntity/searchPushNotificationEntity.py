from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Helper.entityHelper import EntityHelper
from Searcher.pushNotificationSearcher import PushNotificationSearcher
from protobuff.pushnotification_pb2 import PushNotificationSearchResponsePb


class States(Enum):
    START = 0,
    GET_SEARCH = 1,
    FORM_RESPONSE = 2,
    DONE = 3,


class PushNotificationSearchEntity:
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_searchHandler = PushNotificationSearcher()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None
    Resp = None
    pushNotificationSearchResponse = PushNotificationSearchResponsePb()

    def start(self, pushNotificationSearchReqPb):
        self.builder = pushNotificationSearchReqPb
        self.controlFlow(currentState=States.GET_SEARCH)

    def done(self):
        return self.Resp

    def getSearch(self):
        pushNotificatonResp = self.m_searchHandler.handle(pushNotificationSearchPb=self.builder)
        if (pushNotificatonResp != None):
            self.Resp = pushNotificatonResp
        self.controlFlow(currentState=States.FORM_RESPONSE)

    def getFormResponse(self):
        if (self.Resp != None):
            self.Resp = self.m_helper.pushNotificationResponse(pushNotificationResp=self.Resp)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_SEARCH):
            self.getSearch()
        elif (currentState == States.FORM_RESPONSE):
            self.getFormResponse()
        elif (currentState == States.DONE):
            self.done()
