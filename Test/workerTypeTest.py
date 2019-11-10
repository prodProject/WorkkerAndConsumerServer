from google.protobuf.json_format import MessageToJson

from Services.workerTypeService import WorkerTypeService
from protobuff.entity_pb2 import ACTIVE
from protobuff.workertype_pb2 import WorkerTypeSearchRequestPb, CONSTRUCTOR

m_woker = WorkerTypeService()

m_searchReq = WorkerTypeSearchRequestPb()
m_searchReq.dbInfo.lifeTime = ACTIVE
m_searchReq.workerType = CONSTRUCTOR
print(MessageToJson(m_searchReq))
