class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        r = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        c = [[0 for _ in xrange(len(matrix[0]))] for _ in xrange(len(matrix))]
        ans = 0
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == "1":
                    r[i][j] = r[i - 1][j] + 1
                    c[i][j] = c[i][j - 1] + 1
                    if r[i][j] > m[i - 1][j - 1] and c[i][j] > m[i - 1][j - 1]:
                        m[i][j] = m[i - 1][j - 1] + 1
                    else:
                        m[i][j] = min(r[i][j], c[i][j])
                    if m[i][j] > ans:
                        ans = m[i][j]
        return ans ** 2

t = Solution()

assert t.maximalSquare(["1"]) == 1

matrix = [
    "10100",
    "10111",
    "11111",
    "10010",
]

assert t.maximalSquare(matrix) == 4

matrix = [
    "11100",
    "11100",
    "11111",
    "01111",
    "01111",
    "01111"
]

assert t.maximalSquare(matrix) == 16
