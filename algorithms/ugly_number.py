class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        not_primes = []
        UGLY_FACTORS = [2, 3, 5]

        for factor in UGLY_FACTORS:
            while num % factor == 0:
                num /= factor

        return True if num == 1 else False

def test():
    a = Solution()
    assert(a.isUgly(1))
    assert(a.isUgly(2))
    assert(a.isUgly(3))
    assert(a.isUgly(5))
    assert(a.isUgly(6))
    assert(a.isUgly(8))
    assert(not a.isUgly(214797179))
    assert(not a.isUgly(14))
    assert(not a.isUgly(21))
    assert(not a.isUgly(22))
    return 'test passed'

print test()
