from google.protobuf import json_format

from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.workerService import WorkerService
from protobuff import worker_pb2
from protobuff.entity_pb2 import StatusEnum
from protobuff.worker_pb2 import WorkerPb

service = WorkerService()
json = ConvertPbToJSON()
builder = WorkerPb()
builder.dbInfo.lifeTime = StatusEnum.DELETED
#print(json.converPbtojsonStringWithProperFormat(builder=builder))
# print(json.converPbtojsonString(builder=builder))
#print(service.update(id=builder.dbInfo.id,builder=builder))
#print(service.create(builder=builder))
print(json_format.Parse('{"dbInfo": {"lifeTime": "DELETED"}}', worker_pb2.WorkerPb(), ignore_unknown_fields=False))
'''pbjson = MessageToJson(builder)
stringjson = str(json.dumps(pbjson))
formattedstringjson = stringjson
formattedstringjson = formattedstringjson.replace('\\n', '')
formattedstringjson = formattedstringjson.replace('\\', '')
formattedstringjson = formattedstringjson.replace(" ", "")
# formattedstringjson = formattedstringjson[0].replace('"', "'")
# formattedstringjson = formattedstringjson[len(formattedstringjson) - 1].replace('"', "'")
counter = 0;
finaljson = ""
for i in formattedstringjson:
    if (counter == 0):
        finaljson += "'"
    elif (counter == len(formattedstringjson) - 1):
        finaljson += "'"
    else:
        finaljson += i
    counter += 1

print(finaljson)'''
