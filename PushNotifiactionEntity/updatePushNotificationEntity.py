from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Comparetor.pushNotificationComparetor import PushNotificationComparetor
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from PushNotifiactionEntity.getPushNotificationEntity import GetPushNotificationEntity


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    COMPARE_PB = 2
    UPDATE_ENTITY_ID = 3,
    DONE = 4,


class UpdatePushNotificationEntity:
    m_helper = EntityHelper()
    m_getEntity = GetPushNotificationEntity()
    m_queryExecutor = QueryExecuter()
    m_converterPbToJson = ConvertPbToJSON()
    m_converterJsonToPb = ConvertJSONToPb()
    m_comparePushNotificationPb = PushNotificationComparetor()
    oldPb = None
    builder = None
    id = None

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
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.COMPARE_PB):
            self.comaprePb()
        elif (currentState == States.UPDATE_ENTITY_ID):
            self.updateEntity()
        elif (currentState == States.DONE):
            self.done()
