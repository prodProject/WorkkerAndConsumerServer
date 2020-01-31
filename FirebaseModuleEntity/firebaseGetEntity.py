from enum import Enum

from FirebaseModuleEntity.firebaseEntity import FirebaseEntity


class States(Enum):
    START = 0,
    GET_ENTITY = 1,
    DONE = 2,


class FirebaseGetEntity:
    m_firebase = FirebaseEntity()

    id = None
    firebaseEnum = None
    response = None

    def start(self, firebaseEnum, id):
        self.id = id
        self.firebaseEnum = firebaseEnum
        self.controlFlow(currentState=States.GET_ENTITY)

    def done(self):
        return self.response

    def getEntity(self):
        resp = self.m_firebase.get(firebaseEntityEnum=self.firebaseEnum, id=self.id)
        if (resp != None):
            self.response = resp
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY):
            self.getEntity()
        elif (currentState == States.DONE):
            self.done()
