from distutils.command.install import install
from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from Enums.firebaseEntityEnum import FirebaseEntityEnum
from Services.firebaseDatabaseService import FirebaseDatabaseService
from protobuff.verification_pb2 import VerificationPb


class States(Enum):
    START = 0,
    GET_ENTITY = 1,
    CONVERT_TO_PB =2;
    DONE = 3,


class VerificationGetEntity:
    m_firebase = FirebaseDatabaseService()
    m_convertor = ConvertJSONToPb()

    id = None
    response = None

    def start(self, id):
        self.id = id
        self.controlFlow(currentState=States.GET_ENTITY)

    def done(self):
        return self.response

    def getEntity(self):
        resp = self.m_firebase.get(firebaseEnum=FirebaseEntityEnum.VERIFICATIONCODE.name, id=self.id)
        if (resp != None):
            self.response = resp
        self.controlFlow(currentState=States.CONVERT_TO_PB)

    def convertPb(self):
        resp = self.m_convertor.converjsontoPBProper(response=self.response,instanceType=VerificationPb())
        if(resp!=None):
            self.response=resp
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY):
            self.getEntity()
        elif (currentState == States.CONVERT_TO_PB):
            self.convertPb()
        elif (currentState == States.DONE):
            self.done()
