from enum import Enum

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from CommonCode.passwordHashOrDehashHelper import PasswordHasherOrDeHasher
from CommonCode.queryExecutor import QueryExecuter
from Enums.databaseTables import Tables
from Enums.passwordEnum import PasswordMode
from Helper.entityHelper import EntityHelper
from Password.passwordHelper import PasswordHelper
from protobuff import worker_pb2


class States(Enum):
    START = 0,
    GET_PASSWORD_MODE = 1,
    GENEREATE_PASSWORD = 2,
    VERIFY_PASSWORD = 3,
    DONE = 4,


class GenereateAndVerifyPassword:
    m_helper = PasswordHelper()
    m_passwordEncrytorOrDecryptor = PasswordHasherOrDeHasher();

    pb = None
    mode = None

    def start(self, pb, mode):
        self.pb = pb
        self.mode = mode
        self.controlFlow(currentState=States.GET_PASSWORD_MODE)

    def done(self):
        return self.pb

    def getPasswordMode(self):
        if (self.mode == PasswordMode.GENERATE_PASSWORD):
            self.controlFlow(currentState=States.GENEREATE_PASSWORD)
        elif (self.mode == PasswordMode.VERIFY_PASSWORD):
            self.controlFlow(currentState=States.VERIFY_PASSWORD)
        else:
            self.controlFlow(currentState=States.DONE)

    def getGenreatePassword(self):
        self.pb.password = self.m_passwordEncrytorOrDecryptor.getHashFromPassword(
            password=self.m_helper.getPasswordFromLoginPb(loginPb=self.pb))
        self.controlFlow(currentState=States.DONE)


    def getVerifyPassWord(self):
        self.pb.password = self.m_passwordEncrytorOrDecryptor.getHashFromPassword(
            password=self.m_helper.getPasswordFromLoginPb(loginPb=self.pb))

    def controlFlow(self, currentState):
        if (currentState == States.GET_PASSWORD_MODE):
            self.getPasswordMode()
        elif (currentState == States.GENEREATE_PASSWORD):
            self.getGenreatePassword()
        elif (currentState == States.VERIFY_PASSWORD):
            self.getVerifyPassWord()
        elif (currentState == States.DONE):
            self.done()
