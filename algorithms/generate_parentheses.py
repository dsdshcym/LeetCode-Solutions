class Solution(object):
    def dfs(self, s, n, m):
        if n == 0 and m == 0:
            self.ans.append(s)
            return
        if n > 0:
            self.dfs(s + "(", n - 1, m + 1)
        if m > 0:
            self.dfs(s + ")", n, m - 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs("", n, 0)
        return self.ans

def test():
    t = Solution()

    assert t.generateParenthesis(3) == \
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
