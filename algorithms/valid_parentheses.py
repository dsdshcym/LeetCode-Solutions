class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if c in pair:
                if (not stack) or (stack[-1] != pair[c]):
                    return False
                else:
                    stack.pop(-1)
            else:
                stack.append(c)
        if stack:
            return False
        return True

t = Solution()
assert(t.isValid('()'))
assert(t.isValid('({[]})'))
assert(not t.isValid('([)]'))
assert(not t.isValid('(]]])'))
assert(not t.isValid('{{{'))
assert(not t.isValid(']'))
print("tests passed")
