import json
import urllib.request

my_data = dict()
#my_data["email"] = "shivani222329@gmail.com"
#my_data["password"] = "123456"
my_data["idToken"] = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjUxMjRjY2JhZDVkNWZiZjNiYTJhOGI1ZWE3MTE4NDVmOGNiMjZhMzYiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvZC1wcm9qZWN0LWMzYTdiIiwiYXVkIjoicHJvZC1wcm9qZWN0LWMzYTdiIiwiYXV0aF90aW1lIjoxNTc4MTM1ODE2LCJ1c2VyX2lkIjoiQmpvd284cU9SSE9jVDFTS3FNeW9CME9LQUxIMyIsInN1YiI6IkJqb3dvOHFPUkhPY1QxU0txTXlvQjBPS0FMSDMiLCJpYXQiOjE1NzgxMzU4MTYsImV4cCI6MTU3ODEzOTQxNiwiZW1haWwiOiJzaGl2YW5pMjIyMzI5QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzaGl2YW5pMjIyMzI5QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.g6FKwATYfeQxRlaXA1MSwzdxwf5wf3WvOwnhEevCCaINyQWNrZZJxZYNzB68Wsd7KacxkblgTQ-VPiED7mToEnpPZ6dQUXioobpQZTMskPucjQQGqdHwwi73DFrnClWNLSB0CmQL9h7p9jpWQJ7St1gAHX_7WIFKtNtfPEvUBqvTJLxzvAQkrVf9--NhYDRgIaw5IWY-jtchlLzkyhQ1mFunxc-6zyHOfl-gg1TaWm2xk-K1IcbpEpT3qLleGLLYpxWGi_y85dMwz9u0iyPZ7cJ4TWWFF_o3FBbi50lzr9MJu18C7GlDsmg7IEbcTDCNcKhJWYvHSto6NQjdsRbKng"

json_data = json.dumps(my_data).encode()
headers = {"Content-Type": "application/json"}
request = urllib.request.Request(
    "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=" + "AIzaSyCHyTXyqa0B8f-bsCPQgCAd22d17Mehmko", data=json_data,
    headers=headers)

try:
    loader = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    message = json.loads(e.read())
    print(message["error"]["message"])
else:
    print(loader.read())
