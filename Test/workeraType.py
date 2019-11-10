import csv

from google.protobuf.json_format import MessageToJson

from CommonCode.intigerToStringIdConvertor import IntigerToStringIdConverter
from CommonCode.strings import Strings
from Services.workerTypeService import WorkerTypeService
from protobuff.entity_pb2 import ACTIVE
from protobuff.names_pb2 import NamesPb
from protobuff.workertype_pb2 import WorkertypePb, WorkerTypeEnum

converter = IntigerToStringIdConverter()
m_workerType = WorkerTypeService()
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
        workertype.dbInfo.lifeTime = ACTIVE
        listType = list();
        listType.clear()
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
                namePb = NamesPb()
                namePb.canonicalName = Strings.getTittleCaseStringMaker(data=data)
                listType.append(namePb)
                if(data.lower()=='others'):
                    workertype.categories.extend(listType)
                    break
        #print(MessageToJson(workertype))
        print(m_workerType.create(builder=workertype))
        j=0

finally:
    f.close()
