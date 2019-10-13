from google.protobuf.json_format import MessageToJson

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
worker.contactDetails.email.localPart = 'shubhamtiwaricr07'
worker.contactDetails.email.domain = 'gmail.com'
worker.contactDetails.primaryMobile.code = ISD_91
worker.contactDetails.primaryMobile.number = '1'
mobile =worker.contactDetails.secondryMobile.add()
mobile.code = ISD_91
mobile.number = '1'
worker.type.personType = WORKER
worker.device.macId = '19:68:15:c4:77:ad'
worker.device.osType = 'ANDROID'
worker.device.model = 'Redmi'
worker.device.deviceName = 'H@cker'
workerReg.worker.CopyFrom(worker)
workerReg.password = 'new'
print(service.registration(registrationRequestPb=workerReg))
