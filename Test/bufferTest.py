from google.protobuf.json_format import MessageToJson

from Services.loginService import LoginService
from Services.registrationWorkerService import RegistrationWorkerService
from protobuff.entity_pb2 import ACTIVE
from protobuff.mobile_pb2 import ISD_91
from protobuff.persontypeenum_pb2 import WORKER
from protobuff.registration_pb2 import RegistrationRequestPb
from protobuff.worker_pb2 import WorkerPb
service = RegistrationWorkerService()
workerReg =RegistrationRequestPb()
worker  = WorkerPb()
worker.dbInfo.lifeTime = ACTIVE
worker.name.firstName = 'shubham'
worker.name.lastName = 'tiwari'
worker.contactDetails.email.localPart = 'shubhamtiwari'
worker.contactDetails.email.domain = 'gmail.com'
worker.contactDetails.primaryMobile.code = ISD_91
worker.contactDetails.primaryMobile.number = '9621019232'
mobile =worker.contactDetails.secondryMobile.add()
mobile.code = ISD_91
mobile.number = '8687598496'
worker.type.personType = WORKER
worker.device.macId = '19:68:45:c4:d1:ad'
worker.device.osType = 'ANDROID'
worker.device.model = 'Redmi'
worker.device.deviceName = 'H@cker'
workerReg.worker.CopyFrom(worker)
workerReg.password = 'new'
#print(service.registration(registrationRequestPb=workerReg))
m_login = LoginService()
print(m_login.get(id="kH"))
