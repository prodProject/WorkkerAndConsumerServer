# start
# get count
# done
from enum import Enum
from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from protobuff import worker_pb2


class States(Enum):
    Start = 0,
    GET_COUNT = 1,
    DONE = 2,


class CountWorkerEntity:
    m_queryExecutor = QueryExecuter()
    workerserchPb = worker_pb2.WorkerPb()
    m_converterJsonToPb = ConvertJSONToPb()

    builder = None

    def start(self, workerserchPb):
        self.builder = workerserchPb
        self.controlFlow(currentState=States.GET_COUNT)

    def done(self):
        return self.workerConutResponse

    def getCount(self):
        workerPb = self.m_queryExecutor.count(table="WORKER_DATA", subquery="raw_data IS NOT NULL")
        if (workerPb != None):
            self.builder = self.m_convertJsontoPb.converjsontoPBProper(response=workerPb,
                                                                       instanceType=worker_pb2.WorkerPb())

        # self.m_queryExecutor.count(table, subquery)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_COUNT):
            self.getCount()
        elif (currentState == States.DONE):
            self.done()
