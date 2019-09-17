from google.protobuf.json_format import MessageToJson

from Handlers.workerHandler import WorkerHandler
from WorkerEntity.searchWorkerEntity import WorkerSearchEntity
from protobuff.entity_pb2 import ACTIVE, DELETED
from protobuff.workersearch_pb2 import WorkerSearchRequestPb
service = WorkerSearchEntity()
req = WorkerSearchRequestPb()
req.lifeTime = DELETED
service.start(workerPb=req)
print(MessageToJson(service.done()))
