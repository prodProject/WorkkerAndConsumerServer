from google.protobuf.json_format import MessageToJson

from protobuff.gender_pb2 import UNKNOWN_GENDER


class GenderComparetor:

    def comapreGenderPb(self, oldPb, newPb):
        if (oldPb.gender != UNKNOWN_GENDER):
            if (newPb.gender != UNKNOWN_GENDER):
                None  # nothing
            else:
                assert False, "Gender Cannot be UNKNOWN_GENDER type" + MessageToJson(newPb)
