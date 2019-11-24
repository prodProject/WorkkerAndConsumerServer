from google.protobuf.json_format import MessageToJson

from protobuff.mobile_pb2 import UNKNOWN_CODE


class MobileComparetor:

    def comapreMobilePb(self, oldPb, newPb):
        if (oldPb.number != ''):
            if (newPb.number != ''):
                None
            else:
                assert False, self.errorString(errorString="Number", newPb=newPb)
        if (oldPb.code != UNKNOWN_CODE):
            if (newPb.code != UNKNOWN_CODE):
                None  # nothing
            else:
                assert False, "Code Cannot be UNKNOWN_CODE type" + MessageToJson(newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
