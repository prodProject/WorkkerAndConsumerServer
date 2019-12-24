from enum import Enum

from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Helper.entityHelper import EntityHelper
from Services.entityService import EntityService
#improt proto file of consumer
# from protobuff.worker_pb2 import WorkerPb

from Enums.databaseTables import Tables
# from Database.createTableIfNotExixts import States


class States(Enum):
     START = 0,
     GET_ENTITY_ID = 1,
     CREATE_CONSUMER_ENTITY = 2,
     DONE = 3,

class CreateConsumerEntity:
    m_entityId = EntityService()
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_converter = ConvertPbToJSON()
    #use bulider for consumer insted of worker
    #builder = WorkerPb()
    id = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def getEntityId(self):
        self.id = self.m_entityId.get()
        self.controlFlow(currentState=States.CREATE_CONSUMER_ENTITY)

    def createEntityId(self):
        consumerEntity = self.m_helper.createEntity(id=self.id, builder=self.builder)
        self.builder = self.m_queryExecutor.create(builder=consumerEntity, table=Tables.CONSUMER_DATA.name)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.CREATE_CONSUMER_ENTITY):
            self.createEntityId()
        elif (currentState == States.DONE):
            self.done()
