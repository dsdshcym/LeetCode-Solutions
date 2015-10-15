from itertools import permutations

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        NUMS = '123456789'
        return ''.join(list(permutations(NUMS[:n]))[k - 1])

t = Solution()

assert t.getPermutation(3, 1) == '123'
assert t.getPermutation(3, 2) == '132'
assert t.getPermutation(3, 3) == '213'
assert t.getPermutation(3, 4) == '231'
assert t.getPermutation(3, 5) == '312'

print "tests passed"
