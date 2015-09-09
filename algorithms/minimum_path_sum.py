class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MAXINT = 9223372036854775807
        n = len(grid)
        m = len(grid[0])
        min_sum = [[MAXINT for _ in range(m)] for _ in range(n)]
        min_sum[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if (i > 0):
                    min_sum[i][j] = min(min_sum[i][j], min_sum[i - 1][j] + grid[i][j])
                if (j > 0):
                    min_sum[i][j] = min(min_sum[i][j], min_sum[i][j - 1] + grid[i][j])
        return min_sum[-1][-1]

t = Solution()
g = [[1, 2], [0, 1]]
print t.minPathSum(g)
