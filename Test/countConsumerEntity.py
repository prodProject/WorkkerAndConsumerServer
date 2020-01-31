from Services.consumerService import ConsumerService
from WorkerEntity.countWorkerEntity import CountWorkerEntity

service = ConsumerService()

# print(service.start(table="WORKER_DATA", subquery="raw_data IS NOT NULL"))

print(service.count(builder=None))
