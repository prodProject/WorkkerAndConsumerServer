from Services.workerService import WorkerService
from protobuff.entity_pb2 import ACTIVE
from protobuff.mobile_pb2 import ISD_91
from protobuff.persontypeenum_pb2 import WORKER
from protobuff.worker_pb2 import WorkerPb

service = WorkerService()
worker  = WorkerPb()
worker.dbInfo.id = "F"
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
print(service.get(id="F"))
