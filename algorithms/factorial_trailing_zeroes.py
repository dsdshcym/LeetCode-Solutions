class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(1, n + 1):
            if 5 ** i > n:
                break
            ans += n // (5 ** i)
        return ans

t = Solution()
assert(t.trailingZeroes(5) == 1)
assert(t.trailingZeroes(10) == 2)
assert(t.trailingZeroes(30) == 7)
assert(t.trailingZeroes(100) == 24)
print("tests passed")
