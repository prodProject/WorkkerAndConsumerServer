from enum import Enum

from FirebaseModuleEntity.firebaseEntity import FirebaseEntity


class States(Enum):
    START = 0,
    UPDATE_ENTITY = 1,
    DONE = 2,


class FirebaseUpdateEntity:
    m_firebase = FirebaseEntity()

    data = None
    id = None
    firebaseEnum = None
    response = None

    def start(self, firebaseEnum, id, data):
        self.data = data
        self.id = id
        self.firebaseEnum = firebaseEnum
        self.controlFlow(currentState=States.UPDATE_ENTITY)

    def done(self):
        return self.id

    def updateEntity(self):
        resp = self.m_firebase.update(firebaseEntityEnum=self.firebaseEnum, id=self.id, data=self.data)
        if (resp != None):
            self.response = self.data
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.UPDATE_ENTITY):
            self.updateEntity()
        elif (currentState == States.DONE):
            self.done()
