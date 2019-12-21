from google.protobuf.json_format import MessageToJson

from BasicCache.BasicCacheModule import BasicCache
from CommonCode.convertJSONTOPb import ConvertJSONToPb
from CommonCode.convertPbToJSON import ConvertPbToJSON
from Services.workerService import WorkerService
from protobuff import worker_pb2


class WorkerCache(BasicCache):
    m_workerService = WorkerService();
    m_convertorJsonToPb = ConvertJSONToPb()
    m_convertorPbToJson = ConvertPbToJSON()

    def getUnchecked(self, key):
        if (self.get(key=key) != None):
            return self.m_convertorJsonToPb.converjsontoPBProper(response=self.get(key=key),
                                                                 instanceType=worker_pb2.WorkerPb())
        else:
            self.set(key=key,
                     value=self.m_convertorPbToJson.converPbtojsonString(builder=self.m_workerService.get(id=key)))
        return self.m_convertorJsonToPb.converjsontoPBProper(response=self.get(key=key),
                                                             instanceType=worker_pb2.WorkerPb())
