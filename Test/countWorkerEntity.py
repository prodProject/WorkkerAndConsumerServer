
from WorkerEntity.countWorkerEntity import CountWorkerEntity

service = CountWorkerEntity

# print(service.start(table="WORKER_DATA", subquery="raw_data IS NOT NULL"))

print(service.getCount())