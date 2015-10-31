class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True for _ in xrange(n)]
        primes[0] = primes[1] = False
        ans = 0
        for i in xrange(n):
            if primes[i]:
                ans += 1
                for j in xrange(i, n):
                    if i * j >= n:
                        break
                    primes[i * j] = False
        return ans

t = Solution()

assert t.countPrimes(1) == 0
assert t.countPrimes(2) == 0
assert t.countPrimes(3) == 1
assert t.countPrimes(4) == 2
assert t.countPrimes(5) == 2
