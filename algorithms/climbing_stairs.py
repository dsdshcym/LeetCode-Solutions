class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1, 1]
        for i in range(2, n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]

t = Solution()
assert(t.climbStairs(2) == 2)
assert(t.climbStairs(3) == 3)
assert(t.climbStairs(4) == 5)
assert(t.climbStairs(5) == 8)
assert(t.climbStairs(6) == 13)
print("tests passed")
