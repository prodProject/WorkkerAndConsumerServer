from Database.databaseHelper import DatabaseHelper
from WorkerEntity import countWorkerEntity


from CommonCode import queryExecutor


q=queryExecutor.QueryExecuter.count(table="WORKER_DATA",subquery="raw_data IS NOT NULL")

print(q)