class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        half = 0
        while half < x:
            half, x = half * 10 + x % 10, x // 10
        return x in (half, half // 10)

t = Solution()
assert(t.isPalindrome(0))
assert(t.isPalindrome(1))
assert(t.isPalindrome(101))
assert(not t.isPalindrome(10))
assert(not t.isPalindrome(23))
print("tests passed")
