from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Helper.entityHelper import EntityHelper
from Searcher.consumerSearcher import ConsumerSearcher
from protobuff.consumer_pb2 import ConsumerSearchResponsePb


class States(Enum):
    START = 0,
    GET_SEARCH = 1,
    FORM_RESPONSE = 2,
    DONE = 3,


class ConsumerSearchEntity:
    m_helper = EntityHelper()
    m_query = QueryExecuter()
    m_searchHandler = ConsumerSearcher()
    m_converterPbtoJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None
    consumerResp = None
    consumerSearchResponse = ConsumerSearchResponsePb()

    def start(self, consumersearchreqPb):
        self.builder = consumersearchreqPb
        self.controlFlow(currentState=States.GET_SEARCH)

    def done(self):
        return self.consumerSearchResponse

    def getSearch(self):
        consumerResp = self.m_searchHandler.handle(consumerpb=self.builder)
        if (consumerResp != None):
            self.consumerResp = consumerResp
        self.controlFlow(currentState=States.FORM_RESPONSE)

    def getFormResponse(self):
        if (self.consumerResp != None):
            self.consumerSearchResponse = self.m_helper.consumerRespose(consumerResp=self.consumerResp)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_SEARCH):
            self.getSearch()
        elif (currentState == States.FORM_RESPONSE):
            self.getFormResponse()
        elif (currentState == States.DONE):
            self.done()
