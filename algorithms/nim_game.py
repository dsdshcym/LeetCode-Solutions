class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0

t = Solution()

assert not t.canWinNim(4)
assert t.canWinNim(3)

print "tests passed"
