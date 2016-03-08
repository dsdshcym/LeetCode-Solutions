# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#     return True if version > 10 else False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        return r

# t = Solution()
# for i in range(11, 100):
#     assert t.firstBadVersion(i) == 11
# print "test passed"
