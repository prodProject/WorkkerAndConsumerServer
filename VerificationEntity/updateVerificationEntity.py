from enum import Enum

from Enums.firebaseEntityEnum import FirebaseEntityEnum
from Services.firebaseDatabaseService import FirebaseDatabaseService


class States(Enum):
    START = 0,
    UPDATE_ENTITY = 1,
    DONE = 2,


class VerificationUpdateEntity:
    m_firebase = FirebaseDatabaseService()

    data = None
    response = None

    def start(self, data):
        self.data = data
        self.controlFlow(currentState=States.UPDATE_ENTITY)

    def done(self):
        return self.response

    def updateEntity(self):
        resp = self.m_firebase.update(firebaseEnum=FirebaseEntityEnum.VERIFICATIONCODE.name,
                                      id=self.data.workerRef.dbInfo.id, data=self.data)
        if (resp != None):
            self.response = self.data
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.UPDATE_ENTITY):
            self.updateEntity()
        elif (currentState == States.DONE):
            self.done()
