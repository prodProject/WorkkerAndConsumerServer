import csv

from google.protobuf.json_format import MessageToJson

from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from protobuff.workertype_pb2 import WorkertypePb, WorkerTypeEnum

converter = IntigerToStringIdConverter()
f = open("../WorkerTypeSheet.csv", 'rt')
try:
    reader = csv.reader(f)
    i=0
    for row in reader:
        if(i<2):
            i=i+1
            continue
        j=0
        workertype = WorkertypePb()
        for data in row:
            if(j==0):
                workertype.dbInfo.id = converter.convert(id=int(data))
                j=j+1
                continue
            if(j==1):
                workertype.workerType= WorkerTypeEnum.Value(str(data))
                j=j+1
                continue
            if(j>1):
                workertype.categories.add().canonicalName = data.lower()
                if(data.lower()=='others'):
                    break
        print(MessageToJson(workertype))
        j=0

finally:
    f.close()
