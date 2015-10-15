from math import factorial

class Solution(object):
    def getStrPermutation(self, n_str, k):
        n = len(n_str)
        if n == 1:
            return n_str[0]
        r = (k - 1) / factorial(n - 1)
        new_k = k - r * factorial(n - 1)
        digit = n_str[r]
        n_str.remove(digit)
        return digit + self.getStrPermutation(n_str, new_k)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        n_str = [str(i) for i in range(1, n + 1)]
        return self.getStrPermutation(n_str, k)

t = Solution()

assert t.getPermutation(3, 1) == '123'
assert t.getPermutation(3, 2) == '132'
assert t.getPermutation(3, 3) == '213'
assert t.getPermutation(3, 4) == '231'
assert t.getPermutation(3, 5) == '312'

print "tests passed"
