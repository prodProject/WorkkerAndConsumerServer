import json

from google.protobuf import json_format
from google.protobuf.json_format import MessageToJson


class ConvertPbToJSON:

    def converPbtojson(self, builder):
        return MessageToJson(builder)

    def converPbtojsonString(self, builder):
        pbjson = MessageToJson(builder)
        stringjson = str(json.dumps(pbjson))
        formattedstringjson = stringjson
        formattedstringjson = formattedstringjson.replace('\\n', '')
        formattedstringjson = formattedstringjson.replace('\\', '')
        formattedstringjson = formattedstringjson.replace(" ", "")
        counter = 0;
        finaljson = ""
        for i in formattedstringjson:
            if (counter == 0):
                finaljson += "'"
            elif (counter == len(formattedstringjson) - 1):
                finaljson += "'"
            else:
                finaljson += i
            counter += 1
        return finaljson


    def converPbtojsonStringWithProperFormat(self, builder):
        pbjson = MessageToJson(builder)
        stringjson = str(json.dumps(pbjson))
        formattedstringjson = stringjson
        formattedstringjson = formattedstringjson.replace('\\n', '')
        formattedstringjson = formattedstringjson.replace('\\', '')
        formattedstringjson = formattedstringjson.replace(" ", "")
        return formattedstringjson
