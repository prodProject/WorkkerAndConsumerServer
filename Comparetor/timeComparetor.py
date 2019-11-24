from google.protobuf.json_format import MessageToJson

from protobuff.time_pb2 import UNKNOWN_TIME_ZONE


class TimeComparetor:

    def compareTimePb(self, oldPb, newPb):
        if (oldPb.date != ''):
            if (newPb.date != ''):
                None
            else:
                assert False, self.errorString(errorString="Date", newPb=newPb)
        if (oldPb.month != ''):
            if (newPb.month != ''):
                None
            else:
                assert False, self.errorString(errorString="Month", newPb=newPb)

        if (oldPb.year != ''):
            if (newPb.year != ''):
                None
            else:
                assert False, self.errorString(errorString="Year", newPb=newPb)

        if (oldPb.formattedDate != ''):
            if (newPb.formattedDate != ''):
                None
            else:
                assert False, self.errorString(errorString="Formatted Date", newPb=newPb)

        if (oldPb.milliseconds != 0):
            if (newPb.milliseconds != 0):
                None
            else:
                assert False, self.errorString(errorString="Milliseconds", newPb=newPb)

        if (oldPb.timezone != UNKNOWN_TIME_ZONE):
            if (newPb.timezone != UNKNOWN_TIME_ZONE):
                None  # nothing
            else:
                assert False, "TimeZone Cannot be UNKNOWN_TIME_ZONE type" + MessageToJson(newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
