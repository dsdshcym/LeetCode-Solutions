class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.matrix_sum = [[]]
            return

        n, m = len(matrix), len(matrix[0])
        self.matrix_sum = [[0 for j in range(m)] for i in range(n)]

        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                self.matrix_sum[i][j] = matrix[i][j] + \
                                        self.get_sum(i - 1, j) + \
                                        self.get_sum(i, j - 1) - \
                                        self.get_sum(i - 1, j - 1)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.get_sum(row2, col2) -\
            self.get_sum(row1 - 1, col2) -\
            self.get_sum(row2, col1 - 1) +\
            self.get_sum(row1 - 1, col1 - 1)

    def get_sum(self, row, col):
        if not self.matrix_sum or not self.matrix_sum[0]:
            return 0
        if row < 0 or col < 0 or row >= len(self.matrix_sum) or col >= len(self.matrix_sum[0]):
            return 0
        return self.matrix_sum[row][col]

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
assert(numMatrix.sumRegion(2, 1, 4, 3) == 8)
assert(numMatrix.sumRegion(1, 1, 2, 2) == 11)
assert(numMatrix.sumRegion(1, 2, 2, 4) == 12)
print("tests passed")
