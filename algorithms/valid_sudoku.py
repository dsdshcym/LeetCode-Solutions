#!/usr/bin/python3

from operator import and_
from functools import reduce
from pprint import pprint

class Solution(object):
    def validate(self, L):
        count = {}
        for c in L:
            count.setdefault(c, 0)
            count[c] += 1
        for c in count:
            if count[c] > 1 and c != '.':
                return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        RANGE9 = range(9)
        RANGE3 = range(3)
        to_be_validated = [board[i] for i in RANGE9] + \
                          [[board[i][j] for i in RANGE9] for j in RANGE9] + \
                          [[board[i + x * 3][j + y * 3] for i in RANGE3 for j in RANGE3]
                           for x in RANGE3 for y in RANGE3]
        return reduce(and_, map(self.validate, to_be_validated))

t = Solution()
board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]
assert(t.isValidSudoku(board))
print("tests passed")
