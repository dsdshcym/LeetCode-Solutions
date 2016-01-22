import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        N = len(s)
        for i in range(N):
            if s[i] != s[N-i-1]:
                return False
        return True

t = Solution()
assert(t.isPalindrome("A man, a plan, a canal: Panama"))
assert(not t.isPalindrome("0P"))
assert(not t.isPalindrome("race a car"))
print("tests passed")
