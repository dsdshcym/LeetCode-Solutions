class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_values = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.min_values.append(x)
        else:
            self.min_values.append(min(x, self.min_values[-1]))
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.min_values.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_values[-1]
