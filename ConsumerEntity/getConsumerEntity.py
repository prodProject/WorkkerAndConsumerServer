from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from protobuff import consumer_pb2
from protobuff.consumer_pb2 import ConsumerPb


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    DONE = 2,


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
        consumerPb = self.m_queryExecutor.get(id=self.id, table=Tables.CONSUMER_DATA.name)
        if (consumerPb != None):
            self.builder = self.m_converterJsonToPb.converjsontoPBProper(response=consumerPb,
                                                                         instanceType=consumer_pb2.ConsumerPb())
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.DONE):
            self.done()
