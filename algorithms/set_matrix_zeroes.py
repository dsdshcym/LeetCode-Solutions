#+TAG: NEEDS_IMPROVE

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if (matrix == []):
            return matrix
        N = len(matrix)
        M = len(matrix[0])
        zero_row = []
        zero_column = []
        for i in xrange(N):
            for j in xrange(M):
                if (matrix[i][j] == 0):
                    zero_row.append(i)
                    zero_column.append(j)
        for i in xrange(N):
            for j in xrange(M):
                if (i in set(zero_row)) or (j in set(zero_column)):
                    matrix[i][j] = 0

m = [[0, 1], [1, 0]]
t = Solution()
t.setZeroes(m)
print m
