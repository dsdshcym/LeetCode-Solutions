#+TAG: NEEDS_IMPROVE

from collections import defaultdict

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (len(s3) != len(s1) + len(s2)):
            return False
        if len(s1) == 0:
            return s3 == s2
        if len(s2) == 0:
            return s3 == s1
        f = defaultdict(lambda : defaultdict(bool))
        f[0][0] = True
        for i in range(1, len(s3) + 1):
            for j in range(i + 1):
                f[j][i - j] = (j <= len(s1) and s1[j - 1] == s3[i - 1] and f[j - 1][i - j]) or \
                              (i - j <= len(s2) and s2[i - j - 1] == s3[i - 1] and f[j][i - j - 1])
        return f[len(s1)][len(s2)]

t = Solution()
a = 'aabcc'
b = 'dbbca'

assert t.isInterleave(a, b, 'aadbbcbcac')
assert t.isInterleave('', 'b', 'b')
assert t.isInterleave('b', '', 'b')
assert not t.isInterleave(a, b, 'aadbbbaccc')

print "tests passed"
