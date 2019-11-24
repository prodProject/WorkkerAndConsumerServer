from google.protobuf.json_format import MessageToJson

from Services.workerService import WorkerService

m_worker = WorkerService()
worker = m_worker.get(id="ku")
worker.dbInfo.id = ""
print(m_worker.update(id="ku",builder=worker))
