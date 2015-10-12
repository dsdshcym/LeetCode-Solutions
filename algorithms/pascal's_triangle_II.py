from operator import mul
from fractions import Fraction

class Solution(object):
    def nCk(self, n, k):
        return int(reduce(mul, (Fraction(n - i, i + 1) for i in range(k)), 1))

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.nCk(rowIndex, i))
        return ans

t = Solution()

assert t.nCk(5, 0) == 1
assert t.nCk(5, 1) == 5
assert t.nCk(5, 2) == 10
assert t.nCk(5, 3) == 10
assert t.nCk(5, 4) == 5
assert t.nCk(5, 5) == 1

assert t.getRow(3) == [1, 3, 3, 1]

print "tests passed"
