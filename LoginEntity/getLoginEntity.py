from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Helper.entityHelper import EntityHelper
from protobuff import worker_pb2, login_pb2


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    DONE = 2,


class GetLoginEntity:
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

    def getloginEntityId(self):
        loginPb = self.m_queryExecutor.get(id=self.id, table=Tables.LOGIN.name)
        if (loginPb != None):
            self.builder = self.m_converterJsonToPb.converjsontoPBProper(response=loginPb,instanceType=login_pb2.LoginPb())
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getloginEntityId()
        elif (currentState == States.DONE):
            self.done()
