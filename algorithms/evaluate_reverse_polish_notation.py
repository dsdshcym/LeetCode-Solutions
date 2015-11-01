class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        opt = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        for token in tokens:
            if token in '+-*/':
                stack.append(int(opt[token](stack.pop(-2), stack.pop(-1))))
            else:
                stack.append(float(token))
        return int(stack[0])

def test():
    t = Solution()
    assert t.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert t.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert t.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
