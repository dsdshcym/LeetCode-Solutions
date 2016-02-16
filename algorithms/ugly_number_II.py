from sys import maxint

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5]
        queues = {}
        next_prime = {}
        for i, prime in enumerate(primes):
            queues[prime] = []
            if i < len(primes) - 1:
                next_prime[prime] = primes[i+1]
            else:
                next_prime[prime] = None
        first_prime = primes[0]
        queues[first_prime].append(1)
        count = 1
        while count < n:
            count += 1
            min_candidate = maxint
            for prime, queue in queues.items():
                if queue:
                    if queue[0] * prime < min_candidate:
                        min_candidate = queue[0] * prime
                        prime_candidate, queue_candidate = prime, queue
            if queues[first_prime] and queues[first_prime][-1] != min_candidate:
                queues[first_prime].append(min_candidate)
                to_move = queue_candidate.pop(0)
                if next_prime[prime_candidate]:
                    queues[next_prime[prime_candidate]].append(to_move)
                if count == n:
                    return min_candidate
            else:
                to_move = queue_candidate.pop(0)
                if next_prime[prime_candidate]:
                    queues[next_prime[prime_candidate]].append(to_move)
                count -= 1
        return 1

t = Solution()
assert(t.nthUglyNumber(1) == 1)
assert(t.nthUglyNumber(2) == 2)
assert(t.nthUglyNumber(3) == 3)
assert(t.nthUglyNumber(4) == 4)
assert(t.nthUglyNumber(5) == 5)
assert(t.nthUglyNumber(6) == 6)
assert(t.nthUglyNumber(7) == 8)
assert(t.nthUglyNumber(8) == 9)
assert(t.nthUglyNumber(9) == 10)
assert(t.nthUglyNumber(10) == 12)
print("tests passed")
