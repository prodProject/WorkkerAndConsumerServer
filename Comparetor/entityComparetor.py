from google.protobuf.json_format import MessageToJson

from protobuff.entity_pb2 import StatusEnum


class EntityComparetor:

    def campareEntityPb(self, oldPb, newPb):
        if (oldPb.id != ''):
            if (newPb.id != ''):
                if (oldPb.id == newPb.id):
                    None
                else:
                    assert False, "DbInfo Id Cannot be diffrent" + MessageToJson(newPb)
            else:
                assert False, "DbInfo Id Cannot be Empty" + MessageToJson(newPb)

        if (oldPb.lifeTime != StatusEnum.UNKNOWN_STATUS):
            if (newPb.lifeTime != StatusEnum.UNKNOWN_STATUS):
                None  # nothing
            else:
                assert False, "Status Cannot be UNKNOWN type" + MessageToJson(newPb)
