import memcache


# # client = Client(('127.0.0.1', 11211))
# result = client.get('some_key')
# print(result)


class BasicCache:
    client = None

    def __init__(self):
        self.client = memcache.Client([('127.0.0.1', 11255)])
        self.setCache()

    def setCache(self):
        self.client.set('some_key', 'some_value',time=50000)

    def getCache(self):
        self.client.get('some_key')
