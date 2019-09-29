from Services.passwordService import PasswordService
from protobuff.entity_pb2 import ACTIVE
from protobuff.login_pb2 import LoginPb
from protobuff.persontypeenum_pb2 import WORKER, CONSUMER
from protobuff.registration_pb2 import RegistrationResponsePb, USER_EXIST
from protobuff.workersearch_pb2 import WorkerSearchRequestPb


class RegistrationHelper:

    m_passwordService = PasswordService()

    def workerSearchReqBuilder(self, workerPb):
        req = WorkerSearchRequestPb()
        req.mobileNo = workerPb.contactDetails.primaryMobile
        req.lifeTime = ACTIVE
        return req

    def userExixts(self):
        respone = RegistrationResponsePb()
        respone.status  = USER_EXIST
        return respone

    def getLoginPb(self, newRegisterdPb, registrationReq, persontype):
        login = LoginPb()
        login.contactDetails = newRegisterdPb.contactDetails
        login.personType = persontype
        login.workerRef.dbInfo.id = newRegisterdPb.dbInfo.id
        login.workerRef.name = newRegisterdPb.name


        
