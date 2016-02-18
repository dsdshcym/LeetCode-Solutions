import heapq

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :rtype: int
        """
        ugly_numbers = [1]
        count = 1

        def generate(prime):
            for ugly in ugly_numbers:
                yield prime * ugly

        heap = heapq.merge(*map(generate, primes))

        while count < n:
            next_ugly = next(heap)
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
                count += 1

        return ugly_numbers[-1]

t = Solution()
assert(t.nthSuperUglyNumber(2, [2, 3, 5]) == 2)
assert(t.nthSuperUglyNumber(3, [2, 3, 5]) == 3)
assert(t.nthSuperUglyNumber(4, [2, 3, 5]) == 4)
assert(t.nthSuperUglyNumber(5, [2, 3, 5]) == 5)
assert(t.nthSuperUglyNumber(6, [2, 3, 5]) == 6)
assert(t.nthSuperUglyNumber(7, [2, 3, 5]) == 8)
assert(t.nthSuperUglyNumber(8, [2, 3, 5]) == 9)
assert(t.nthSuperUglyNumber(9, [2, 3, 5]) == 10)
assert(t.nthSuperUglyNumber(150, [3, 5, 7, 11, 19, 23, 29, 31, 37, 43, 79, 83,
                                  89, 97, 107, 109, 131, 137, 157, 163, 173,
                                  179, 181, 199, 211, 227, 233, 239, 251, 263])
                                  == 667)
print("tests passed")
