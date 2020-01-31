import json
import urllib.request

my_data = dict()
my_data["email"] = "shivani222329@gmail.com"
my_data["password"] = "123456"
my_data["returnSecureToken"] = True

json_data = json.dumps(my_data).encode()
headers = {"Content-Type": "application/json"}
request = urllib.request.Request(
    "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=" + "AIzaSyCHyTXyqa0B8f-bsCPQgCAd22d17Mehmko", data=json_data,
    headers=headers)

try:
    loader = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    message = json.loads(e.read())
    print(message["error"]["message"])
else:
    print(loader.read())
