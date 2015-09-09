# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# def isBadVersion(version):
#     return True if version > 10 else False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1;
        mid = n / 2;
        right = n;
        while (left < right):
            if (isBadVersion(mid)):
                right = mid;
            else:
                left = mid + 1;
            mid = (left + right) / 2
        return left

# t = Solution()
# for i in range(11, 100):
#     assert t.firstBadVersion(i) == 11
# print "test passed"
