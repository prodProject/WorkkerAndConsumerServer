from protobuff.entity_pb2 import StatusEnum


class WorkerComparetor:

    def workerPbComparetor(self, oldPb, newPb):
        if (oldPb.dbInfo.id != ''):
            if (newPb.dbInfo.id != ''):
                None #nothing
            else:
                assert True, "DbInfo Id Cannot be Empty"
        if (oldPb.dbInfo.lifeTime != StatusEnum.UNKNOWN):
            if (newPb.dbInfo.id != StatusEnum.UNKNOWN):
                None #nothing
            else:
                assert True, "Status Cannot be UNkNOWN type"
