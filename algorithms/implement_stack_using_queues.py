from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_queue = deque()
        self.temp_queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.main_queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.main_queue) > 1:
            self.temp_queue.append(self.main_queue.popleft())
        val = self.main_queue.popleft()
        while len(self.temp_queue) > 0:
            self.main_queue.append(self.temp_queue.popleft())
        return val

    def top(self):
        """
        :rtype: int
        """
        while len(self.main_queue) > 1:
            self.temp_queue.append(self.main_queue.popleft())
        val = self.main_queue[0]
        self.temp_queue.append(self.main_queue.popleft())
        while len(self.temp_queue) > 0:
            self.main_queue.append(self.temp_queue.popleft())
        return val

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.main_queue) == 0

t = Stack()
assert t.empty()
t.push(1)
assert not t.empty()
assert t.top() == 1
assert not t.empty()
t.push(2)
assert t.pop() == 2
assert t.pop() == 1

print "tests passed"
