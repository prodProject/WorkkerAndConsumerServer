from enum import Enum

from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from Services.entityService import EntityService
from Services.workerService import WorkerService
from protobuff.pushnotification_pb2 import PushNotificationPb


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    CREATE_PUSH_NOTIFICATION_ENTITY = 2,
    UPDATE_WORKER =3,
    DONE = 4,


class CreatePushNotificationEntity:
    m_entityId = EntityService()
    m_workerService = WorkerService();
    m_helper = EntityHelper()
    m_queryExecutor = QueryExecuter()
    m_converter = ConvertPbToJSON()
    builder = PushNotificationPb()
    id = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def done(self):
        return self.builder

    def getEntityId(self):
        self.id = self.m_entityId.get()
        self.controlFlow(currentState=States.CREATE_PUSH_NOTIFICATION_ENTITY)

    def createEntityId(self):
        pushNotificationEntity = self.m_helper.createEntity(id=self.id, builder=self.builder)
        self.builder = self.m_queryExecutor.create(builder=pushNotificationEntity,table=Tables.PUSH_NOTIFICATON.name)
        if(self.builder!=None):
            self.controlFlow(currentState=States.UPDATE_WORKER)
        else:
            self.controlFlow(currentState=States.DONE)

    def updateWorker(self):
        workerPb = self.m_workerService.get(id=self.builder.workerRef.dbInfo.id)
        workerPb.pushNotificationRef.dbInfo.id = self.builder.dbInfo.id
        workerPb.pushNotificationRef.name.canonicalName = self.builder.tokenId
        self.m_workerService.update(id=workerPb.dbInfo.id,builder=workerPb)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.CREATE_PUSH_NOTIFICATION_ENTITY):
            self.createEntityId()
        elif (currentState == States.UPDATE_WORKER):
            self.updateWorker()
        elif (currentState == States.DONE):
            self.done()
