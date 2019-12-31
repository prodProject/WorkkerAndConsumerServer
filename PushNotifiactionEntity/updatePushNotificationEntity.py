from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Comparetor.pushNotificationComparetor import PushNotificationComparetor
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from PushNotifiactionEntity.getPushNotificationEntity import GetPushNotificationEntity
from Services.workerService import WorkerService


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    COMPARE_PB = 2
    UPDATE_ENTITY_ID = 3,
    GET_WORKER = 4,
    UPDATE_PUSHNOTIFICATION_IN_WORKER = 5,
    DONE = 6,


class UpdatePushNotificationEntity:
    m_helper = EntityHelper()
    m_workerService = WorkerService()
    m_getEntity = GetPushNotificationEntity()
    m_queryExecutor = QueryExecuter()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    m_comparePushNotificationPb = PushNotificationComparetor()
    oldPb = None
    builder = None
    id = None
    m_worker = None;

    def start(self, id, builder):
        self.id = id
        self.builder = builder
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def done(self):
        return self.builder

    def getEntityId(self):
        self.m_getEntity.start(id=self.id)
        self.oldPb = self.m_getEntity.done()
        if (self.oldPb == None):
            self.controlFlow(currentState=States.DONE)
        self.controlFlow(currentState=States.COMPARE_PB)

    def comaprePb(self):
        self.m_comparePushNotificationPb.comaprePushNotifiactionPb(oldPb=self.oldPb, newPb=self.builder)
        self.controlFlow(currentState=States.UPDATE_ENTITY_ID)

    def updateEntity(self):
        newPb = self.m_queryExecutor.update(id=self.id, builder=self.builder, table=Tables.PUSH_NOTIFICATON.name)
        self.builder = newPb
        self.controlFlow(currentState=States.GET_WORKER)

    def getWorker(self):
        worker = self.m_workerService.get(id=self.builder.workerRef.dbInfo.id)
        if (worker != None):
            self.m_worker = worker;
        self.controlFlow(currentState=States.UPDATE_PUSHNOTIFICATION_IN_WORKER)

    def updateWorker(self):
        self.m_worker.pushNotificationRef.name.canonicalName = self.builder.tokenId;
        worker = self.m_workerService.update(id=self.m_worker.dbInfo.id, builder=self.m_worker)
        if (worker != None):
            self.m_worker = worker;
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.COMPARE_PB):
            self.comaprePb()
        elif (currentState == States.UPDATE_ENTITY_ID):
            self.updateEntity()
        elif (currentState == States.GET_WORKER):
            self.getWorker()
        elif (currentState == States.UPDATE_PUSHNOTIFICATION_IN_WORKER):
            self.updateWorker()
        elif (currentState == States.DONE):
            self.done()
