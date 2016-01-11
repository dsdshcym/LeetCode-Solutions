class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return n == 1

t = Solution()
assert t.isPowerOfThree(3**0)
assert t.isPowerOfThree(3**1)
assert t.isPowerOfThree(3**2)
assert t.isPowerOfThree(3**3)
assert t.isPowerOfThree(3**4)
assert t.isPowerOfThree(3**5)
assert t.isPowerOfThree(3**6)
assert not t.isPowerOfThree(4)
assert not t.isPowerOfThree(5)
assert not t.isPowerOfThree(6)
assert not t.isPowerOfThree(7)

print "test passed"
