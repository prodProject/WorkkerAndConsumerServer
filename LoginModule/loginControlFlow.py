from enum import Enum


from LoginModule.loginHelper import LoginHelper
from Services.loginService import LoginService
from Services.workerService import WorkerService
from protobuff.login_pb2 import LoginResponsePb
from protobuff.persontypeenum_pb2 import WORKER
from protobuff.responsestatusenum_pb2 import SUCCESS, USER_NOT_REGISTRED


class States(Enum):
    START = 0,
    CHECK_LOGIN_EXISTS = 1,
    GET_WORKER = 2,
    GET_CONSUMER = 3,
    DONE = 4,


class Login:
    m_loginService = LoginService();
    m_workerService = WorkerService();
    m_helper = LoginHelper()
    id = None
    m_loginReq = None
    m_response = LoginResponsePb();

    def start(self, loginReq):
        assert loginReq is not None, "LoginRequestPb cannot be empty"
        self.m_loginReq = loginReq
        self.controlFlow(currentState=States.CHECK_LOGIN_EXISTS)

    def done(self):
        return self.m_response

    def getLoginExists(self):
        searchRequest = self.m_helper.getLoginSearchReqbuestBuilder(loginPb=self.m_loginReq.login)
        respone = self.m_loginService.search(builder=searchRequest)
        if (respone.summary.totalHits > 0):
            self.m_response.status.statusType = SUCCESS
            if(self.m_loginReq.login.personType.personType == WORKER):
                self.controlFlow(currentState=States.GET_WORKER)
            else:
                self.controlFlow(currentState=States.GET_CONSUMER)
        else:
            self.m_response.status.statusType = USER_NOT_REGISTRED
            self.controlFlow(currentState=States.DONE)

    def getWorker(self):
        worker = self.m_workerService.get(id=self.m_loginReq.workerRef.dbInfo.id)
        if (worker != None):
            self.m_response.worker.CopyFrom(worker)
        self.controlFlow(currentState=States.DONE)

    def getConsumer(self):
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.CHECK_LOGIN_EXISTS):
            self.getLoginExists()
        elif (currentState == States.GET_WORKER):
            self.getWorker()
        elif (currentState == States.GET_CONSUMER):
            self.getConsumer()
        elif (currentState == States.DONE):
            self.done()
