from collections import deque

class Solution(object):
    def calc(self, s):
        a, b = 0, 0
        V = {'(': +1, ')': -1}
        for c in s:
            a += V.get(c, 0)
            b += a < 0
            a = max(0, a)
        return a + b

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = set([s])
        queue = deque([s])
        ans = set()
        while queue:
            current = queue.popleft()
            miss_parentheses = self.calc(current)
            if miss_parentheses == 0:
                ans.add(current)
                continue
            for i in range(len(current)):
                next_string = current[:i] + current[i+1:]
                if next_string not in visited and self.calc(next_string) < miss_parentheses:
                    visited.add(next_string)
                    queue.append(next_string)
        return list(ans)

t = Solution()
print(t.removeInvalidParentheses("()())()"))
print(t.removeInvalidParentheses(")(((((((("))
