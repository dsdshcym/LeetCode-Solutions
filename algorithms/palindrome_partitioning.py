class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        attempt = []

        def dfs(i, s):
            if i >= len(s):
                ans.append(list(attempt))
                return
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    attempt.append(s[i:j])
                    dfs(j, s)
                    attempt.pop()

        dfs(0, s)
        return ans

t = Solution()
assert(t.partition("a") == [["a"]])
print("tests passed")
