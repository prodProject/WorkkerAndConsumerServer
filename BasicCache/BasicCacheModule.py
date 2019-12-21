from werkzeug.contrib.cache import SimpleCache


class BasicCache:
    cache = SimpleCache()

    def set(self, key, value):
        self.cache.set(key, value, timeout=50 * 1000)

    def get(self, key):
        return self.cache.get(key=key)
