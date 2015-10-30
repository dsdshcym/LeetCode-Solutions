from collections import deque

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = deque()
        self.value = dict()

    def get(self, key):
        """
        :rtype: int
        """
        try:
            self.cache.remove(key)
        except ValueError:
            return -1
        self.cache.append(key)
        return self.value[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        try:
            self.cache.remove(key)
        except ValueError:
            if len(self.cache) == self.capacity:
                self.cache.popleft()
        self.cache.append(key)
        self.value[key] = value

def test():
    t = LRUCache(2)
    t.set(2,1)
    t.set(1,1)
    assert t.get(2) == 1
    t.set(4,1)
    assert t.get(1) == -1
    assert t.get(2) == 1
