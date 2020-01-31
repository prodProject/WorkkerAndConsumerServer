from enum import Enum

from Services.verificationService import VerificationService


class States(Enum):
    START = 0,
    CREATE_VERIFICATION = 1,
    SEND_EMAIL=2,
    DONE = 3,


class CreateVerification:
    m_service = VerificationService()
    builder = None
    response = None
    id = None

    def start(self, builder):
        self.builder = builder
        self.controlFlow(currentState=States.CREATE_VERIFICATION)

    def done(self):
        return self.response

    def createEntityId(self):
        m_verification = self.m_service.create(data=self.builder)
        if(m_verification!=None):
            self.response = self.builder
            self.controlFlow(currentState=States.SEND_EMAIL)
        self.controlFlow(currentState=States.DONE)

    def sendEmail(self):
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.CREATE_VERIFICATION):
            self.createEntityId()
        elif (currentState == States.SEND_EMAIL):
            self.sendEmail()
        elif (currentState == States.DONE):
            self.done()
