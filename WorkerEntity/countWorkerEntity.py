# start
# get count
# done
from enum import Enum
from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Counter.workerCounter import WorkerCounter
from Enums.databaseTables import Tables
from Searcher.workerSearcher import WorkerSearcher
from protobuff import worker_pb2
from protobuff.workersearch_pb2 import WorkerSearchRequestPb, WorkerSearchResponsePb


class States(Enum):
    START = 0,
    GET_COUNT = 1,
    DONE = 2,


class CountWorkerEntity:
    m_queryExecutor = QueryExecuter()
    workerserchreqPb = WorkerSearchRequestPb()
    m_converterJsonToPb = ConvertJSONToPb()
    workerserchresPb = WorkerSearchResponsePb()
    m_countHandler = WorkerCounter()

    builder = None

    def start(self, workerSearchPb):
        self.builder = workerSearchPb
        self.controlFlow(currentState=States.GET_COUNT)

    def done(self):
        return self.workerserchresPb

    def getCount(self):
        workerPb = self.m_countHandler.handle(workerpb=self.builder)
        if (workerPb != None):
            self.workerserchresPb.summary.totalHits=workerPb
        # self.m_queryExecutor.count(table, subquery)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_COUNT):
            self.getCount()
        elif (currentState == States.DONE):
            self.done()
