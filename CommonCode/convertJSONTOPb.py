from google.protobuf import json_format


class ConvertJSONToPb:

    def converjsontoPB(self, response, instanceType):
        return json_format.Parse(response, instanceType, ignore_unknown_fields=False)

    def converjsontoPBProper(self, response, instanceType):
        finaljson = ""
        for i in response:
            if (i == "'"):
                finaljson += '"'
            else:
                finaljson += i
        return json_format.Parse(finaljson, instanceType, ignore_unknown_fields=False)

    def convertToProperjson(self, response):
        finaljson = '"'
        for i in response:
            if (i == "'"):
                finaljson += '"'
            else:
                finaljson += i
        return finaljson
