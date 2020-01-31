import json
from urllib.parse import urlencode

import requests


class HttpReqAndResp:

    def doPost(self,url,data):
        return requests.post(url, data = json.dump(data))

    def doGet(self,url,data):
        return requests.get(url, data = urlencode(data))
