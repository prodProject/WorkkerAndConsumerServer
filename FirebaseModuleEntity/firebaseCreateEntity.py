from enum import Enum

from FirebaseModuleEntity.firebaseEntity import FirebaseEntity


class States(Enum):
    START = 0,
    CREATE_ENTITY = 1,
    DONE = 2,


class FirebaseCreateEntity:
    m_firebase = FirebaseEntity()

    data = None
    id = None
    firebaseEnum = None
    response = None

    def start(self, firebaseEnum, id, data):
        self.data = data
        self.id = id
        self.firebaseEnum = firebaseEnum
        self.controlFlow(currentState=States.CREATE_ENTITY)

    def done(self):
        return self.id

    def createEntity(self):
        resp = self.m_firebase.create(firebaseEntityEnum=self.firebaseEnum, id=self.id, data=self.data)
        if (resp != None):
            self.response = self.data
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.CREATE_ENTITY):
            self.createEntity()
        elif (currentState == States.DONE):
            self.done()
