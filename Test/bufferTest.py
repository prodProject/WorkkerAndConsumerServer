from google.protobuf import json_format

from Services.workerService import WorkerService
from protobuff import worker_pb2
from protobuff.worker_pb2 import WorkerPb

service = WorkerService()
# json = ConvertPbToJSON()
builder = service.get(id="8")
#builder.dbInfo.lifeTime = StatusEnum.ACTIVE
# print(json.converPbtojsonString(builder=builder))
print(builder)

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
