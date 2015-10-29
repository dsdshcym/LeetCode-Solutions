import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = re.match(p, s)
        return m is not None and m.group(0) == s

t = Solution()

assert not t.isMatch("aa","a")
assert t.isMatch("aa","aa")
assert not t.isMatch("aaa","aa")
assert t.isMatch("aa", "a*")
assert t.isMatch("aa", ".*")
assert t.isMatch("ab", ".*")
assert t.isMatch("aab", "c*a*b")
assert not t.isMatch("ab", ".*c")

print "tests passed"
