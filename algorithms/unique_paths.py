from math import factorial

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return factorial(m + n - 2) / factorial(m - 1) / factorial(n - 1)

t = Solution()
assert(t.uniquePaths(3, 7) == 28)
assert(t.uniquePaths(4, 4) == 20)
print("tests passed")
