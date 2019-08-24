from google.protobuf import json_format


class ConvertJSONToPb:

    def converjsontoPB(self, response, instanceType):
        return json_format.Parse(response, instanceType, ignore_unknown_fields=False)

    def converjsontoPBProper(self, response, instanceType):
        finaljson = ""
        finaljson = finaljson+"'"
        for i in response:
            if (i == "'"):
                finaljson += '"'
            else:
                finaljson += i
        finaljson = finaljson+"'"

        print(finaljson)
        return json_format.Parse(finaljson, instanceType, ignore_unknown_fields=False)

    def convertToProperjson(self, response):
        finaljson = '"'
        for i in response:
            if (i == "'"):
                finaljson += '"'
            else:
                finaljson += i
        return finaljson

    def getQuotedJson(self,jsonReq):
        return '"'+str(jsonReq)+'"'
