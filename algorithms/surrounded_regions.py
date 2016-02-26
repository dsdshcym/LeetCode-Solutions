class Solution(object):
    MOVE = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        N, M = len(board), len(board[0])

        queue = []
        for x in range(N):
            queue += [(x, 0), (x, M-1)]
        for y in range(M):
            queue += [(0, y), (N-1, y)]

        while queue:
            x, y = queue.pop(0)
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if board[x][y] == 'O':
                board[x][y] = 'V'
                queue += [(x + move_x, y + move_y)
                          for move_x, move_y in self.MOVE]

        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'

t = Solution()
board = [
    [c for c in "XXXX"],
    [c for c in "XOOX"],
    [c for c in "XXOX"],
    [c for c in "XOXX"],
]
t.solve(board)
assert(board == [
    [c for c in "XXXX"],
    [c for c in "XXXX"],
    [c for c in "XXXX"],
    [c for c in "XOXX"],
])

print("tests passed")
