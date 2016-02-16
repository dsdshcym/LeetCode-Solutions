from math import sqrt

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return n
        queue = {n}
        step = 0
        while queue:
            step += 1
            temp = set()
            for x in queue:
                for y in xrange(1, int(sqrt(x)) + 1):
                    if x == y ** 2:
                        return step
                    temp.add(x-y**2)
            queue = temp
        return step

t = Solution()
print(t.numSquares(12))
assert(t.numSquares(12) == 3)
assert(t.numSquares(13) == 2)
print("tests passed")
