class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x, y):
            if x < 0 or x >= N or y < 0 or y >= M:
                return False
            if visited[x][y] or grid[x][y] == '0':
                return False
            visited[x][y] = True
            for dx, dy in move:
                dfs(x+dx, y+dy)
            return True

        if not grid:
            return 0
        ans = 0
        N, M = len(grid), len(grid[0])
        visited = [[False, ] * M for i in range(N)]
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(N):
            for j in range(M):
                if dfs(i, j):
                    ans += 1
        return ans

t = Solution()
map1 = ['11110',
        '11010',
        '11000',
        '00000',]
assert(t.numIslands(map1) == 1)
map2 = ['11000',
        '11000',
        '00100',
        '00011',]
assert(t.numIslands(map2) == 3)
print("tests passed")
