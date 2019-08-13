from enum import Enum

from Database.entityQueryExecuter import EntityQueryExecuter


class States(Enum):
    START = 0,
    GET_ENTITY_ID = 1,
    UPDATE_ENTITY = 2,
    DONE = 3,


class CreateEntity:
    m_exeuctor = EntityQueryExecuter()
    id = None

    def start(self):
        self.controlFlow(currentState=States.GET_ENTITY_ID)

    def done(self):
        return self.id

    def getEntityId(self):
        self.id = self.m_exeuctor.execute()
        self.controlFlow(currentState=States.UPDATE_ENTITY)

    def upadteId(self):
        self.m_exeuctor.update()
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.UPDATE_ENTITY):
            self.upadteId()
        elif (currentState == States.DONE):
            self.done()
