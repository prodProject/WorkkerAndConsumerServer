from enum import Enum

from Enums.firebaseEntityEnum import FirebaseEntityEnum
from Services.firebaseDatabaseService import FirebaseDatabaseService


class States(Enum):
    START = 0,
    CREATE_ENTITY = 1,
    DONE = 2,


class VerificationCreateEntity:
    m_firebase = FirebaseDatabaseService()

    data = None
    response = None

    def start(self, data):
        self.data = data
        self.controlFlow(currentState=States.CREATE_ENTITY)

    def done(self):
        return self.response

    def createEntity(self):
        resp = self.m_firebase.create(firebaseEnum=FirebaseEntityEnum.VERIFICATIONCODE.name,
                                      id=self.data.workerRef.dbInfo.id, data=self.data)
        if (resp != None):
            self.response = self.data
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.CREATE_ENTITY):
            self.createEntity()
        elif (currentState == States.DONE):
            self.done()
