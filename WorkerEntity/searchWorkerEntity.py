from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from Searcher.workerSearcher import WorkerSearcher
from protobuff import worker_pb2
from protobuff.workersearch_pb2 import WorkerSearchResponsePb


class States(Enum):
    START = 0,
    GET_SEARCH = 1,
    FORM_RESPONSE = 2,
    DONE = 3,


class WorkerSearchEntity:
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_searchHandler = WorkerSearcher()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None
    workerResp = None
    workerSearchResponse = WorkerSearchResponsePb()

    def start(self, workerPb):
        self.builder = workerPb
        self.controlFlow(currentState=States.GET_SEARCH)

    def done(self):
        return self.workerSearchResponse

    def getSearch(self):
        workerResp = self.m_searchHandler.handle(workerpb=self.builder)
        if (workerResp != None):
            self.workerResp = workerResp
        self.controlFlow(currentState=States.FORM_RESPONSE)

    def getFormResponse(self):
        if (self.workerResp != None):
            self.workerSearchResponse = self.m_helper.workerResponse(workerResp=self.workerResp)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_SEARCH):
            self.getSearch()
        elif (currentState == States.FORM_RESPONSE):
            self.getFormResponse()
        elif (currentState == States.DONE):
            self.done()
