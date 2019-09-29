from enum import Enum

from RegisrationModule.registrationHelper import RegistrationHelper
from Services.emailService import EmailService
from Services.workerService import WorkerService
from protobuff.persontypeenum_pb2 import WORKER, CONSUMER


class States(Enum):
    START = 0,
    CHECK_WORKER_EXISTS = 1,
    CHECK_CONSUMER_EXISTS = 2,
    CREATE_ENTITY_IN_DB = 3,
    CREATE_ENTITY_IN_LOGIN = 4,
    SEND_MAIL = 5,
    DONE = 6,


class Registration:
    m_workerService = WorkerService()
    m_emailService = EmailService()
    m_helper = RegistrationHelper()
    id = None
    workerPb = None
    response = None
    def start(self,workerPb):
        assert workerPb is not None, "WorkerPb cannot be empty"
        self.workerPb=workerPb
        if(workerPb.type.personType==WORKER):
            self.controlFlow(currentState=States.CHECK_WORKER_EXISTS)
        elif(workerPb.type.personType==CONSUMER):
            self.controlFlow(currentState=States.CHECK_CONSUMER_EXISTS)
        else:
            assert True, "PersonType Cannot defined"


    def done(self):
        return self.id

    def getWorkerIsExists(self):
        searchRequest = self.m_helper.workerSearchReqBuilder(workerPb=self.workerPb)
        respone =  self.m_workerService.search(builder=searchRequest)
        if(respone.summary.totalHits>0):
            self.controlFlow(currentState=States.DONE)
        self.controlFlow(currentState=States.CREATE_ENTITY_IN_DB)

    def upadteId(self):
        self.m_exeuctor.update()
        self.controlFlow(currentState=States.DONE)

    def controlFlow(self, currentState):
        if (currentState == States.GET_ENTITY_ID):
            self.getEntityId()
        elif (currentState == States.UPDATE_ENTITY):
            self.upadteId()
        elif (currentState == States.DONE):
            self.done()
