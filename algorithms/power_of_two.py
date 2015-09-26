class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n != 0) and (abs(n) == (n & (-n)))

t = Solution()

assert(t.isPowerOfTwo(1))
assert(t.isPowerOfTwo(2))
assert(t.isPowerOfTwo(4))
assert(t.isPowerOfTwo(8))
assert(t.isPowerOfTwo(-1024))
assert(not t.isPowerOfTwo(0))
assert(not t.isPowerOfTwo(6))
assert(not t.isPowerOfTwo(7))
assert(not t.isPowerOfTwo(9))
assert(not t.isPowerOfTwo(-10))

print "Tests passed"
