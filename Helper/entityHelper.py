from CommonCode.convertJSONTOPb import ConvertJSONToPb
from protobuff import worker_pb2, login_pb2, workertype_pb2, pushnotification_pb2
from protobuff.entity_pb2 import ACTIVE
from protobuff.login_pb2 import LoginSearchRespsonsePb
from protobuff.pushnotification_pb2 import PushNotificationSearchResponsePb
from protobuff.workersearch_pb2 import WorkerSearchResponsePb
from protobuff.workertype_pb2 import WorkerTypeSearchResponsePb


class EntityHelper:
    m_converterJsonToPb = ConvertJSONToPb()
    workerlist = list()
    pushNotificationList = list()
    workerTypelist = list()

    def createEntity(self, id, builder):
        builder.dbInfo.id = id
        builder.dbInfo.lifeTime = ACTIVE
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
                self.workerlist.append(self.m_converterJsonToPb.converjsontoPBProper(response=worker[0],
                                                                                     instanceType=worker_pb2.WorkerPb()))
            except ValueError:
                pass
        workerSearchResponse.results.extend(self.workerlist)
        return workerSearchResponse

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
        self.pushNotificationList.clear()
        loginSearchResponse = LoginSearchRespsonsePb()
        loginSearchResponse.summary.totalHits = len(loginResp)
        for index, login in enumerate(loginResp):
            # workerSearchResponse.results.add()
            try:
                self.pushNotificationList.append(
                    self.m_converterJsonToPb.converjsontoPBProper(response=login[0], instanceType=login_pb2.LoginPb()))
            except ValueError:
                pass
        loginSearchResponse.results.extend(self.pushNotificationList)
        return loginSearchResponse


    def pushNotificationResponse(self, pushNotificationResp):
        self.pushNotificationList.clear()
        pushNotificationSearchResponse = PushNotificationSearchResponsePb()
        pushNotificationSearchResponse.summary.totalHits = len(pushNotificationResp)
        for index, pushNotification in enumerate(pushNotificationResp):
            # workerSearchResponse.results.add()
            try:
                self.pushNotificationList.append(
                    self.m_converterJsonToPb.converjsontoPBProper(response=pushNotification[0], instanceType=pushnotification_pb2.PushNotificationPb()))
            except ValueError:
                pass
        pushNotificationSearchResponse.results.extend(self.pushNotificationList)
        return pushNotificationSearchResponse
