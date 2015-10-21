#+TAG: NEEDS_REVIEW

LIVE = 1
DEAD = 0

class Solution(object):
    def __init__(self):
        m = [-1, 0, 1]
        self.moves = [(i, j) for i in m
                     for j in m
                     if not (i == 0 and j == 0)]

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        N = len(board)
        M = len(board[0])
        need_change = []
        for i in xrange(N):
            for j in xrange(M):
                live = 0
                for dx, dy in self.moves:
                    x, y = dx + i, dy + j
                    if (not (0 <= x < N)) or (not (0 <= y < M)):
                        continue
                    live += board[x][y]
                if board[i][j] == LIVE:
                    if live == 2 or live == 3:
                        continue
                    need_change.append((i, j))
                else:
                    if live == 3:
                        need_change.append((i, j))
        for i, j in need_change:
            board[i][j] = 1 - board[i][j]

board = [[1 for _ in xrange(3)] for _ in xrange(3)]
t = Solution()
t.gameOfLife(board)
print board
