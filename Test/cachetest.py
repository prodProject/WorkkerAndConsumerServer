# import memcache


# # client = Client(('127.0.0.1', 11211))
# result = client.get('some_key')
# print(result)
from werkzeug.contrib.cache import SimpleCache


class BasicCache:
    client = None

    def __init__(self):
        self.client = SimpleCache()
        self.setCache()
        print('hello')


    def setCache(self):
        self.client.set('some_key', 'some_value',timeout=50000)

    def getCache(self):
        self.client.get('some_key')
        print(self.client.get('some_key'))
