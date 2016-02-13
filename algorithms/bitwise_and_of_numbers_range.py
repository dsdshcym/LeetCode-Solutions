from math import log

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == m:
            return m
        return n & m & (-(1 << int(log(n - m, 2) + 1)))

t = Solution()
assert(t.rangeBitwiseAnd(5, 7) == 4)
assert(t.rangeBitwiseAnd(4, 8) == 0)
print("tests passed")
