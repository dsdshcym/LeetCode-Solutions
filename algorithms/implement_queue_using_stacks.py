class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [[], []]
        self.current_stack = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack[self.current_stack].append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self._switch_stacks(self.stack[self.current_stack],
                            self.stack[1 - self.current_stack])
        self.stack[1 - self.current_stack].pop()
        self._switch_stacks(self.stack[1 - self.current_stack],
                            self.stack[self.current_stack])

    def peek(self):
        """
        :rtype: int
        """
        self._switch_stacks(self.stack[self.current_stack],
                            self.stack[1 - self.current_stack])
        value = self.stack[1 - self.current_stack][-1]
        self._switch_stacks(self.stack[1 - self.current_stack],
                            self.stack[self.current_stack])
        return value

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack[self.current_stack]

    def _switch_stacks(self, stackA, stackB):
        while stackA:
            stackB.append(stackA.pop())
