class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans.append(temp)
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
