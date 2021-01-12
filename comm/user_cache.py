from module.login import check_local_status

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

    def __getitem__(self, key):
        return self.cache[key]

def init_mine():
    d={
        "user_info":check_local_status()
    }
    return user_cache(**d)


mine = init_mine()
