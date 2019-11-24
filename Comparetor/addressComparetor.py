from google.protobuf.json_format import MessageToJson


class AddressComparetor:

    def compareAddressPb(self, oldPb, newPb):
        if (oldPb.houseNo != ''):
            if (newPb.houseNo != ''):
                None
            else:
                assert False, self.errorString(errorString="House Number", newPb=newPb)
        if (oldPb.streetOrRoad != ''):
            if (newPb.streetOrRoad != ''):
                None
            else:
                assert False, self.errorString(errorString="Street Or Road", newPb=newPb)

        if (oldPb.landmark != ''):
            if (newPb.landmark != ''):
                None
            else:
                assert False, self.errorString(errorString="Land Mark", newPb=newPb)

        if (oldPb.pincode != ''):
            if (newPb.pincode != ''):
                None
            else:
                assert False, self.errorString(errorString="Pincode", newPb=newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
