class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r - 1:
            mid = (l + r) // 2
            if mid ** 2 > x:
                r = mid
            else:
                l = mid
        if r ** 2 <= x:
            return r
        return l

t = Solution()
assert(t.mySqrt(0) == 0)
assert(t.mySqrt(1) == 1)
assert(t.mySqrt(2) == 1)
assert(t.mySqrt(3) == 1)
assert(t.mySqrt(4) == 2)
print("tests passed")
