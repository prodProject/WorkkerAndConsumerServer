from google.protobuf.json_format import MessageToJson

from protobuff.persontypeenum_pb2 import UNKNOWN_PERSON_TYPE


class PersonTypeComparetor:

    def comaprePersonTypePb(self, oldPb, newPb):
        if (oldPb.personType != UNKNOWN_PERSON_TYPE):
            if (newPb.personType != UNKNOWN_PERSON_TYPE):
                None  # nothing
            else:
                assert False, "PersonType Cannot be UNKNOWN_PERSON_TYPE type" + MessageToJson(newPb)
