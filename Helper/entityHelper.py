from CommonCode.convertJSONTOPb import ConvertJSONToPb
from protobuff import worker_pb2, login_pb2, workertype_pb2, consumer_pb2
from protobuff.consumer_pb2 import ConsumerSearchResponsePb
from protobuff.login_pb2 import LoginSearchRespsonsePb
from protobuff.workersearch_pb2 import WorkerSearchResponsePb
from protobuff.workertype_pb2 import WorkerTypeSearchResponsePb


class EntityHelper:
    m_converterJsonToPb = ConvertJSONToPb()
    workerlist = list()
    consumerlist = list()
    loginlist = list()
    workerTypelist = list()

    def createEntity(self, id, builder):
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
        for index, worker in enumerlistate(workerResp):
            # workerSearchResponse.results.add()
            try:
                self.workerlist.append(self.m_converterJsonToPb.converjsontoPBProper(response=worker[0],
                                                                                     instanceType=worker_pb2.WorkerPb()))
            except ValueError:
                pass
        workerSearchResponse.results.extend(self.workerlist)
        return workerSearchResponse

    def consumerRespose(self, consumerResp):
        self.consumerlist.clear()
        consumerSerchResponse = ConsumerSearchResponsePb()
        consumerSerchResponse.summary.totalHits = len(consumerResp)
        for index, consumer in enumerate(consumerResp):
            # ConumerSearchResponse.results.add()
            try:
                self.workerlist.append(self.m_converterJsonToPb.converjsontoPBProper(response=consumer[0],
                                                                                     instanceType=consumer_pb2.ConsumerPb()))
            except ValueError:
                pass
        consumerSerchResponse.results.extend(self.workerlist)
        return consumerSerchResponse

    def workerTypeResponse(self, workerTpeResp):
        self.workerTypelist.clear()
        workerTyepSearchResponse = WorkerTypeSearchResponsePb()
        workerTyepSearchResponse.summary.totalHits = len(workerTpeResp)
        for index, worker in enumerate(workerTpeResp):
            # workerSearchResponse.results.add()
            try:
                self.workerTypelist.append(self.m_converterJsonToPb.converjsontoPBProper(response=worker[0],
                                                                                         instanceType=workertype_pb2.WorkerTypePb()))
            except ValueError:
                pass
        workerTyepSearchResponse.results.extend(self.workerTypelist)
        return workerTyepSearchResponse

    def loginResponse(self, loginResp):
        self.loginlist.clear()
        loginSearchResponse = LoginSearchRespsonsePb()
        loginSearchResponse.summary.totalHits = len(loginResp)
        for index, login in enumerate(loginResp):
            # workerSearchResponse.results.add()
            try:
                self.loginlist.append(
                    self.m_converterJsonToPb.converjsontoPBProper(response=login[0], instanceType=login_pb2.LoginPb()))
            except ValueError:
                pass
        loginSearchResponse.results.extend(self.loginlist)
        return loginSearchResponse
