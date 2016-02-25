class Solution(object):
    def is_palindrome(self, s):
        return s == s[::-1]

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if self.is_palindrome(s):
            return 0

        for i in range(1, len(s)):
            if self.is_palindrome(s[i:]) and self.is_palindrome(s[:i]):
                return 1

        cut = [i for i in xrange(-1, len(s)+1)]
        for i in xrange(len(s)):
            for j in xrange(i, len(s)+1):
                if self.is_palindrome(s[i:j+1]):
                    cut[j+1] = min(cut[j+1], cut[i]+1)
        return cut[-1]

t = Solution()
assert(t.minCut("aab") == 1)
assert(t.minCut("coder") == 4)
print("tests passed")
