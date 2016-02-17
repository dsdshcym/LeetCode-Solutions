class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        paths = []
        for i, row in enumerate(obstacleGrid):
            paths.append([0,] * len(row))
            for j, obstacle in enumerate(row):
                if obstacle:
                    continue
                if i == 0 and j == 0 and not obstacle:
                    paths[i][j] = 1
                    continue
                if i > 0:
                    paths[i][j] += paths[i - 1][j]
                if j > 0:
                    paths[i][j] += paths[i][j - 1]
        return paths[i][j]

t = Solution()
test_case = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
assert(t.uniquePathsWithObstacles(test_case) == 2)
print("tests passed")
