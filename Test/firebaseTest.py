import json
import urllib.request
import urllib.error

my_data = dict()
my_data["email"] = "shubhamtiwaricr07@gmail.com"
my_data["requestType"] = "PASSWORD_RESET"

json_data = json.dumps(my_data).encode()
headers = {"Content-Type": "application/json"}
request = urllib.request.Request("https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key="+"AIzaSyCHyTXyqa0B8f-bsCPQgCAd22d17Mehmko", data=json_data, headers=headers)

try:
    loader = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    print("fail")
    print(e.args)
else:
    print("success")
    print(loader.read())
