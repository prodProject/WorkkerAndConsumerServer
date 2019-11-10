from enum import Enum

from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from Services.entityService import EntityService


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    CREATE_WORKER_TYPE_ENTITY = 2,
    DONE = 3,

class CreateWorkerTypeEntity:
    m_entityId = EntityService()
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    builder = None
    id = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.CREATE_WORKER_TYPE_ENTITY)

    def done(self):
        return self.builder

    def getEntityId(self):
        self.id = self.m_entityId.get()
        self.controlFlow(currentState=States.CREATE_WORKER_TYPE_ENTITY)

    def createEntityId(self):
        #workerTypeEntity = self.m_helper.createEntity(id=self.id, builder=self.builder)
        self.builder = self.m_queryExecutor.create(builder=self.builder,table=Tables.WORKER_TYPE.name)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.CREATE_WORKER_TYPE_ENTITY):
            self.createEntityId()
        elif (currentState == States.DONE):
            self.done()





