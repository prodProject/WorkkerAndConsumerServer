from enum import Enum

from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from Services.entityService import EntityService
from protobuff.worker_pb2 import WorkerPb


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    CREATE_WORKER_ENTITY = 2,
    DONE = 3,


class CreateWorkerEntity:
    m_entityId = EntityService()
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_converter = ConvertPbToJSON()
    builder = WorkerPb()
    id = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def done(self):
        return self.builder

    def getEntityId(self):
        self.id = self.m_entityId.get()
        self.controlFlow(currentState=States.CREATE_WORKER_ENTITY)

    def createEntityId(self):
        workerEntity = self.m_helper.createEntity(id=self.id, builder=self.builder)
        self.builder = self.m_queryExecutor.create(builder=workerEntity,table=Tables.WORKER_DATA.name)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.CREATE_WORKER_ENTITY):
            self.createEntityId()
        elif (currentState == States.DONE):
            self.done()
