from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Helper.entityHelper import EntityHelper
from Enums.consumerDatabaseTable import Tables



class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    DONE = 3,

class GetConsumerEntity:
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    builder = None
    id = None


    def start(self, id):
        self.id = id
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def done(self):
        return self.builder

    def getEntityId(self):
        workerPb = self.m_queryExecutor.get(id=self.id, table=Tables.CONSUMER_DATA.name)
        if (workerPb != None):
            #proto file error convert worker_pb2 to consumer_pb2
            self.builder = self.m_converterJsonToPb.converjsontoPBProper(response=workerPb,instanceType=worker_pb2.WorkerPb())
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.DONE):
            self.done()