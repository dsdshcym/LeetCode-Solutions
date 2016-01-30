class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        MOVE = [[0, +1], [+1, 0], [0, -1], [-1, 0]]
        ans = [[-1,] * n for i in range(n)]

        def dfs(i, j, d, count):
            if i < 0 or j < 0 or i >= n or j >=n or ans[i][j] != -1:
                return False
            ans[i][j] = count + 1
            new_i, new_j = i + MOVE[d][0], j + MOVE[d][1]
            if not dfs(new_i, new_j, d, count+1):
                d = (d + 1) % 4
                new_i, new_j = i + MOVE[d][0], j + MOVE[d][1]
                if not dfs(new_i, new_j, d, count+1):
                    return False
            return True

        dfs(0, 0, 0, 0)
        return ans

t = Solution()
assert(t.generateMatrix(3) == [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
])
print("tests passed")
