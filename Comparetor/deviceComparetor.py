from google.protobuf.json_format import MessageToJson


class DeviceInfoComaretor:

    def compareDeviceInfoPb(self, oldPb, newPb):
        if (oldPb.macId != ''):
            if (newPb.macId != ''):
                None
            else:
                assert False, self.errorString(errorString="Mac Id", newPb=newPb)
        if (oldPb.osType != ''):
            if (newPb.osType != ''):
                None
            else:
                assert False, self.errorString(errorString="Os Type", newPb=newPb)

        if (oldPb.model != ''):
            if (newPb.model != ''):
                None
            else:
                assert False, self.errorString(errorString="Model", newPb=newPb)

        if (oldPb.deviceName != ''):
            if (newPb.deviceName != ''):
                None
            else:
                assert False, self.errorString(errorString="Device Name", newPb=newPb)

    def errorString(self, errorString, newPb):
        return errorString + "Cannot be Empty" + MessageToJson(newPb)
