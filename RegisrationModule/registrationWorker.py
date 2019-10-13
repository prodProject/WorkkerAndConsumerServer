from enum import Enum

from RegisrationModule.registrationHelper import RegistrationHelper
from Services.emailService import EmailService
from Services.loginService import LoginService
from Services.workerService import WorkerService
from protobuff.registration_pb2 import RegistrationResponsePb


class States(Enum):
    START = 0,
    CHECK_WORKER_EXISTS = 1,
    CREATE_ENTITY_IN_WORKER = 2,
    CREATE_ENTITY_IN_LOGIN = 3,
    SEND_MAIL = 4,
    DONE = 6,


class RegistrationWorker:
    m_workerService = WorkerService()
    m_emailService = EmailService()
    m_loginService = LoginService()
    m_helper = RegistrationHelper()
    id = None
    resgistrationReq = None
    workerPb = None
    response = RegistrationResponsePb();

    def start(self, workerPb):
        assert workerPb is not None, "WorkerPb cannot be empty"
        self.resgistrationReq = workerPb
        self.workerPb = workerPb.worker
        self.controlFlow(currentState=States.CHECK_WORKER_EXISTS)

    def done(self):
        return self.response

    def getWorkerIsExists(self):
        searchRequest = self.m_helper.workerSearchReqBuilder(workerPb=self.workerPb)
        respone = self.m_workerService.search(builder=searchRequest)
        if (respone.summary.totalHits > 0):
            self.respone = self.m_helper.userExixts()
            self.controlFlow(currentState=States.DONE)
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_WORKER)

    def createEntityInWorker(self):
        worker = self.m_workerService.create(builder=self.resgistrationReq.worker)
        if (worker != None):
            self.response.worker.CopyFrom(worker)
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_LOGIN)

    def createEntityInLogin(self):
        login = self.m_loginService.create(
            builder=self.m_helper.getLoginPb(self.response.worker, self.resgistrationReq.worker.type.personType,self.resgistrationReq.password))
        if (login != None):
            self.response.login.CopyFrom(login)
        self.controlFlow(currentState=States.SEND_MAIL)

    def sendMail(self):
        self.m_emailService.send(
            emailbuilder=self.m_helper.getEmailBuilder(emailpb=self.resgistrationReq.worker.contactDetails.email))
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.CHECK_WORKER_EXISTS):
            self.getWorkerIsExists()
        elif (currentState == States.CREATE_ENTITY_IN_WORKER):
            self.createEntityInWorker()
        elif (currentState == States.CREATE_ENTITY_IN_LOGIN):
            self.createEntityInLogin()
        elif (currentState == States.SEND_MAIL):
            self.sendMail()
        elif (currentState == States.DONE):
            self.done()
