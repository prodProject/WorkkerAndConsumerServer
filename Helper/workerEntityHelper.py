import json

from CommonCode.convertJSONTOPb import ConvertJSONToPb
from protobuff import worker_pb2
from protobuff.workersearch_pb2 import WorkerSearchResponsePb


class WorkerEntityHelper:
    m_converterJsonToPb = ConvertJSONToPb()
    workerlist = list()
    def createWorkerEntity(self, id, builder):
        builder.dbInfo.id = id
        return builder

    def comapreIds(self, id1, id2):
        if (id1 == id2):
            return False
        else:
            return True

    def workerResponse(self, workerResp):
        self.workerlist.clear()
        workerSearchResponse = WorkerSearchResponsePb()
        workerSearchResponse.summary.totalHits = len(workerResp)
        for index, worker in enumerate(workerResp):
            # workerSearchResponse.results.add()
            try:
                print(self.m_converterJsonToPb.converjsontoPBProper(response=worker[0],instanceType=worker_pb2.WorkerPb()))
                self.workerlist.append(self.m_converterJsonToPb.converjsontoPBProper(response=worker[0], instanceType=worker_pb2.WorkerPb()))
            except ValueError:
                pass
        workerSearchResponse.results.extend(self.workerlist)
        return workerSearchResponse
