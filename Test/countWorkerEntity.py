from Services.workerService import WorkerService
from WorkerEntity.countWorkerEntity import CountWorkerEntity

service = WorkerService()

# print(service.start(table="WORKER_DATA", subquery="raw_data IS NOT NULL"))

print(service.count(builder=None))
