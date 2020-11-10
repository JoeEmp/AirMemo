class user_cache(object):
    def __init__(self, **kwargs):
        self.cache = dict()
        if kwargs:
            self.cache = kwargs

    def get_value(self, key):
        return self.cache.get(key)

    def del_item(self, key):
        return self.cache.pop(key)

    def clear(self):
        return self.cache.clear()

    def add_item(self, key, value):
        if key not in self.cache.keys():
            self.cache[key] = value

    def update_item(self, key, value):
        self.cache[key] = value

mine = user_cache()
