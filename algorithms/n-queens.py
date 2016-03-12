class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [-1] * n
        results = []
        self.n_queens_helper(0, n, board, results)
        return map(self.board_to_solution, results)

    def n_queens_helper(self, current, size, board, results):
        if current == size:
            results.append(list(board))
            return
        for i in range(size):
            board[current] = i
            if self.no_conflits(current, board):
                self.n_queens_helper(current + 1, size, board, results)

    def no_conflits(self, current, board):
        for i in range(current):
            if board[i] == board[current]:
                return False
            if (current - i) == abs(board[current] - board[i]):
                return False
        return True

    def board_to_solution(self, board):
        n = len(board)
        return ['Q'.rjust(pos + 1, '.').ljust(n, '.')
                for pos in board]

t = Solution()
from pprint import pprint
pprint(t.solveNQueens(4))
