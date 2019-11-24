from google.protobuf.json_format import MessageToJson


class NamesComparetor:

    def compareNamesPb(self, oldPb, newPb):
        if (oldPb.firstName != ''):
            if (newPb.firstName != ''):
                None
            else:
                assert False, self.errorString(errorString="First Name", newPb=newPb)
        if (oldPb.lastName != ''):
            if (newPb.lastName != ''):
                None
            else:
                assert False, self.errorString(errorString="lastName", newPb=newPb)

        if (oldPb.canonicalName != ''):
            if (newPb.canonicalName != ''):
                None
            else:
                assert False, self.errorString(errorString="Canonical Name", newPb=newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
