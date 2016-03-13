class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        stack = []
        self.removeInvalidParentheses_helper(s, 0, "", stack, ans)
        return list(set(ans))

    def removeInvalidParentheses_helper(self, s, index, current, stack, ans):
        if index >= len(s):
            if not stack:
                if ans and len(current) == len(ans[-1]):
                    ans.append(current)
                elif (not ans) or (len(current) > len(ans[-1])):
                    ans[:] = [current]
            return
        if s[index] == '(':
            stack.append('(')
            self.removeInvalidParentheses_helper(s, index + 1, current + '(', stack, ans)
            stack.pop(-1)
            self.removeInvalidParentheses_helper(s, index + 1, current, stack, ans)
        elif s[index] == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
                self.removeInvalidParentheses_helper(s, index + 1, current + ')', stack, ans)
                stack.append('(')
            self.removeInvalidParentheses_helper(s, index + 1, current, stack, ans)
        else:
            self.removeInvalidParentheses_helper(s, index + 1, current + s[index], stack, ans)

t = Solution()
print(t.removeInvalidParentheses("()())()"))
