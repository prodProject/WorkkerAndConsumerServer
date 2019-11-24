from google.protobuf.json_format import MessageToJson


class EmailComparetor:

    def compareEmailPb(self, oldPb, newPb):
        if (oldPb.localPart != ''):
            if (newPb.localPart != ''):
                None
            else:
                assert False, self.errorString(errorString="Local Part", newPb=newPb)
        if (oldPb.domain != ''):
            if (newPb.domain != ''):
                None
            else:
                assert False, self.errorString(errorString="Domain", newPb=newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
