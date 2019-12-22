from google.protobuf.json_format import MessageToJson

from Comparetor.entityComparetor import EntityComparetor
from Comparetor.personTypeComparetor import PersonTypeComparetor
from Comparetor.workerComparetor import WorkerRefComparetor


class PushNotificationComparetor(EntityComparetor, PersonTypeComparetor):

    m_workerRef = WorkerRefComparetor()
    def comaprePushNotifiactionPb(self, oldPb, newPb):
        self.campareEntityPb(oldPb=oldPb.dbInfo, newPb=newPb.dbInfo)
        self.comaprePersonTypePb(oldPb=oldPb.type, newPb=newPb.type)
        self.m_workerRef.compareWorkerRef(oldPb=oldPb.workerRef, newPb=newPb.workerRef)
        if (oldPb.tokenId != ''):
            if (newPb.tokenId != ''):
                None
            else:
                assert False, "token cannoit be empty" + MessageToJson(newPb)
