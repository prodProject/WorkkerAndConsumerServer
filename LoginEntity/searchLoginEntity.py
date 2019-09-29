from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from Searcher.loginSearcher import LoginSearcher
from Searcher.workerSearcher import WorkerSearcher
from protobuff import worker_pb2
from protobuff.login_pb2 import LoginSearchRespsonsePb
from protobuff.workersearch_pb2 import WorkerSearchResponsePb


class States(Enum):
    START = 0,
    GET_SEARCH = 1,
    FORM_RESPONSE = 2,
    DONE = 3,


class LoginSearchEntity:
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_searchHandler = LoginSearcher()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None
    loginResp = None
    loginSearchResponse = LoginSearchRespsonsePb()

    def start(self, loginPb):
        self.builder = loginPb
        self.controlFlow(currentState=States.GET_SEARCH)

    def done(self):
        return self.loginSearchResponse

    def getSearch(self):
        loginResp = self.m_searchHandler.handle(workerpb=self.builder)
        if (loginResp != None):
            self.loginResp = loginResp
        self.controlFlow(currentState=States.FORM_RESPONSE)

    def getFormResponse(self):
        if (self.loginResp != None):
            self.loginSearchResponse = self.m_helper.loginResponse(workerResp=self.loginResp)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_SEARCH):
            self.getSearch()
        elif (currentState == States.FORM_RESPONSE):
            self.getFormResponse()
        elif (currentState == States.DONE):
            self.done()
