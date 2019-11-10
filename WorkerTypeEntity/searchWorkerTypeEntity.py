from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Helper.entityHelper import EntityHelper
from Searcher.workerTypeSearcher import WorkerTypeSearcher
from protobuff.workertype_pb2 import WorkerTypeSearchResponsePb


class States(Enum):
    START = 0,
    GET_SEARCH = 1,
    FORM_RESPONSE = 2,
    DONE = 3,


class WorkerTypeSearchEntity:
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_searchHandler = WorkerTypeSearcher()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None
    workerTypeResp = None
    workerTypeSearchResponse = WorkerTypeSearchResponsePb()

    def start(self, workerTypePb):
        self.builder = workerTypePb
        self.controlFlow(currentState=States.GET_SEARCH)

    def done(self):
        return self.workerTypeSearchResponse

    def getSearch(self):
        workerTypeResp = self.m_searchHandler.handle(workerTypepb=self.builder)
        if (workerTypeResp != None):
            self.workerTypeResp = workerTypeResp
        self.controlFlow(currentState=States.FORM_RESPONSE)

    def getFormResponse(self):
        if (self.workerTypeResp != None):
            self.workerTypeSearchResponse = self.m_helper.workerTypeResponse(workerTpeResp=self.workerTypeResp)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_SEARCH):
            self.getSearch()
        elif (currentState == States.FORM_RESPONSE):
            self.getFormResponse()
        elif (currentState == States.DONE):
            self.done()
