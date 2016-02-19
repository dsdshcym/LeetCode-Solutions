class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        return self.myPow(x * x, n // 2) * [1, x][n % 2]

t = Solution()
assert(t.myPow(1, 10) == 1)
assert(t.myPow(2, 10) == 1024)
print("tests passed")
