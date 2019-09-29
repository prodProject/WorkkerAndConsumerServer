from enum import Enum

from RegisrationModule.registrationHelper import RegistrationHelper
from Services.emailService import EmailService
from Services.loginService import LoginService
from Services.workerService import WorkerService
from protobuff.persontypeenum_pb2 import WORKER, CONSUMER


class States(Enum):
    START = 0,
    CHECK_WORKER_EXISTS = 1,
    CREATE_ENTITY_IN_WORKER = 2,
    CREATE_ENTITY_IN_LOGIN = 3,
    SEND_MAIL = 4,
    DONE = 6,


class Registration:
    m_workerService = WorkerService()
    m_emailService = EmailService()
    m_loginService = LoginService()
    m_helper = RegistrationHelper()
    id = None
    resgistrationReq = None
    response = None
    def start(self,workerPb):
        assert workerPb is not None, "WorkerPb cannot be empty"
        self.resgistrationReq=workerPb
        self.controlFlow(currentState=States.CHECK_WORKER_EXISTS)


    def done(self):
        return self.id

    def getWorkerIsExists(self):
        searchRequest = self.m_helper.workerSearchReqBuilder(workerPb=self.resgistrationReq)
        respone =  self.m_workerService.search(builder=searchRequest)
        if(respone.summary.totalHits>0):
            self.respone = self.m_helper.userExixts()
            self.controlFlow(currentState=States.DONE)
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_WORKER)

    def createEntityInWorker(self):
        worker = self.m_workerService.create(builder=self.resgistrationReq.worker)
        if(worker != None):
            self.respone.worker = worker
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_LOGIN)


    def createEntityInLogin(self):
        worker = self.m_loginService.create(builder=self.resgistrationReq.worker)
        if(worker != None):
            self.respone.worker = worker
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_LOGIN)



    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.UPDATE_ENTITY):
            self.upadteId()
        elif (currentState == States.DONE):
            self.done()
