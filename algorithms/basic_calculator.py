class Solution(object):
    DIGITS = string.digits
    OP_PRESEDENCE = {
        "+": 2,
        "-": 2,
        "(": 1,
        ")": 1,
    }
    OPT = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
    }

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        output_stack, operator_stack = [], []
        num = ""

        for c in s:
            if c == " ":
                continue

            if c in string.digits:
                num += c
            elif num:
                output_stack.append(num)
                num = ""

            if c in self.OP_PRESEDENCE:
                if c == ")":
                    while operator_stack[-1] != "(":
                        output_stack.append(operator_stack.pop(-1))
                    operator_stack.pop(-1)
                elif c == "(":
                    operator_stack.append(c)
                else:
                    while operator_stack and \
                          self.OP_PRESEDENCE[c] <= self.OP_PRESEDENCE[operator_stack[-1]]:
                        output_stack.append(operator_stack.pop(-1))
                    operator_stack.append(c)

        if num:
            output_stack.append(num)

        while operator_stack:
            output_stack.append(operator_stack.pop(-1))

        stack = list()
        opt = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
        }
        for token in output_stack:
            if token in '+-*/':
                stack.append(int(self.OPT[token](stack.pop(-2), stack.pop(-1))))
            else:
                stack.append(float(token))
        return int(stack[0])

t = Solution()
assert(t.calculate("2-(5-6)") == 3)
assert(t.calculate("1 + 1") == 2)
assert(t.calculate(" 2-1 + 2 ") == 3)
assert(t.calculate("(1+(4+5+2)-3)+(6+8)") == 23)
print("tests passed")
