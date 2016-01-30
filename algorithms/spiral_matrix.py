class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        MOVE = [[0, +1], [+1, 0], [0, -1], [-1, 0]]
        M, N = len(matrix), len(matrix[0])
        visited = [[False,] * N for i in range(M)]
        ans = []

        def dfs(i, j, d):
            if i < 0 or j < 0 or i >= M or j >=N or visited[i][j]:
                return False
            ans.append(matrix[i][j])
            visited[i][j] = True
            new_i, new_j = i + MOVE[d][0], j + MOVE[d][1]
            if not dfs(new_i, new_j, d):
                d = (d + 1) % 4
                new_i, new_j = i + MOVE[d][0], j + MOVE[d][1]
                if not dfs(new_i, new_j, d):
                    return False
            return True

        dfs(0, 0, 0)
        return ans

t = Solution()
assert(t.spiralOrder([[1]]) == [1])
assert(t.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3])
print("tests passed")
