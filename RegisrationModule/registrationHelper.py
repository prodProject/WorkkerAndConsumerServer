from ConstantsProperties import sendGridEmailProperties
from Enums.passwordEnum import PasswordMode
from Services.passwordService import PasswordService
from TimeUtility.timeUtill import TimeUtil
from protobuff.email_pb2 import EmailBuilderPb, EmailIdPb
from protobuff.entity_pb2 import ACTIVE
from protobuff.login_pb2 import LoginPb
from protobuff.pushnotification_pb2 import PushNotificationPb
from protobuff.registration_pb2 import RegistrationResponsePb
from protobuff.responsestatusenum_pb2 import USER_EXIST
from protobuff.time_pb2 import TimeZoneEnum
from protobuff.workersearch_pb2 import WorkerSearchRequestPb


class RegistrationHelper:
    m_passwordService = PasswordService()
    m_timeUtility = TimeUtil()

    def workerSearchReqBuilder(self, workerPb):
        req = WorkerSearchRequestPb()
        req.contactDetails.email.localPart =  workerPb.contactDetails.email.localPart
        req.contactDetails.email.domain =  workerPb.contactDetails.email.domain
        req.mobileNo.code = workerPb.contactDetails.primaryMobile.code
        req.mobileNo.number = workerPb.contactDetails.primaryMobile.number
        req.lifeTime = ACTIVE
        return req

    def userExixts(self):
        respone = RegistrationResponsePb()
        respone.status.statusType = USER_EXIST
        return respone

    def getLoginPb(self, newRegisterdPb, persontype,password):
        login = LoginPb()
        login.dbInfo.lifeTime = ACTIVE
        login.contactDetails.CopyFrom(newRegisterdPb.contactDetails)
        login.personType.personType=persontype
        login.workerRef.dbInfo.id = newRegisterdPb.dbInfo.id
        login.workerRef.name.CopyFrom(newRegisterdPb.name)
        login.password = password
        login.timeCreation.CopyFrom(self.m_timeUtility.getTimePb(timeZone=TimeZoneEnum.IST))
        return self.m_passwordService.getOrVerifyPassword(loginpb=login,mode=PasswordMode.GENERATE_PASSWORD)

    def getEmailBuilder(self, emailpb):
        toid = list()
        fromid = sendGridEmailProperties.DEFAULT_EMAIL.split('@')
        emailId = EmailIdPb()
        emailId.localPart = fromid[0]
        emailId.domain = fromid[1]
        emailBuilder = EmailBuilderPb()
        emailBuilder.fromId.CopyFrom(emailId)
        toid.append(emailpb)
        emailBuilder.toId.extend(toid)
        emailBuilder.subject = "Thank you For Registration"
        emailBuilder.content = "We are thanking your for joining us.We definatly take care of you"
        return emailBuilder

    def getPushNotificationPb(self,registration,worker):
         pushNotification = PushNotificationPb();
         pushNotification.workerRef.dbInfo.id = worker.dbInfo.id
         pushNotification.workerRef.name.CopyFrom(worker.name)
         pushNotification.type.CopyFrom(worker.type)
         pushNotification.tokenId = registration.pushNotificationToken;
         return pushNotification;
