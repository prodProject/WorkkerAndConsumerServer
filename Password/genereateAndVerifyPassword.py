from enum import Enum

from CommonCode.passwordHashOrDehashHelper import PasswordHasherOrDeHasher
from Enums.passwordEnum import PasswordMode
from Password.passwordHelper import PasswordHelper
from Services.loginService import LoginService


class States(Enum):
    START = 0,
    GET_PASSWORD_MODE = 1,
    GENEREATE_PASSWORD = 2,
    GET_LOGIN = 3,
    VERIFY_PASSWORD = 4,
    DONE = 5,


class GenereateAndVerifyPassword:
    m_helper = PasswordHelper()
    m_loginService = LoginService()
    m_passwordEncrytorOrDecryptor = PasswordHasherOrDeHasher();
    m_login = None
    pb = None
    mode = None
    m_isValid = False

    def start(self, pb, mode):
        self.pb = pb
        self.mode = mode
        self.controlFlow(currentState=States.GET_PASSWORD_MODE)

    def done(self):
        if (self.mode == PasswordMode.GENERATE_PASSWORD):
            return self.pb
        else:
            return self.m_isValid

    def getPasswordMode(self):
        if (self.mode == PasswordMode.GENERATE_PASSWORD):
            self.controlFlow(currentState=States.GENEREATE_PASSWORD)
        elif (self.mode == PasswordMode.VERIFY_PASSWORD):
            self.controlFlow(currentState=States.GET_LOGIN)
        else:
            self.controlFlow(currentState=States.DONE)

    def getGenreatePassword(self):
        self.pb.password = self.m_passwordEncrytorOrDecryptor.getHashFromPassword(
            password=self.m_helper.getPasswordFromLoginPb(loginPb=self.pb))
        self.controlFlow(currentState=States.DONE)

    def getLogin(self):
        self.m_login = self.m_loginService.get(id=self.pb.dbInfo.id)
        self.controlFlow(currentState=States.VERIFY_PASSWORD)

    def getVerifyPassWord(self):
        self.m_isValid = self.m_passwordEncrytorOrDecryptor.getPasswordFromHash(
            actualPassword=self.m_helper.getPasswordFromLoginPb(loginPb=self.pb),
            hashedPassword=self.m_login.password)
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_PASSWORD_MODE):
            self.getPasswordMode()
        elif (currentState == States.GENEREATE_PASSWORD):
            self.getGenreatePassword()
        elif (currentState == States.GET_LOGIN):
            self.getLogin()
        elif (currentState == States.VERIFY_PASSWORD):
            self.getVerifyPassWord()
        elif (currentState == States.DONE):
            self.done()
