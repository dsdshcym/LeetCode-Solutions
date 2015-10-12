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

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            ans.append(self.getRow(i))
        return ans

t = Solution()
fiveRows = [
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]

assert(t.generate(5) == fiveRows)

print("tests passed")
