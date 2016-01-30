class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []

        x, y = 0, 0
        while m > 0 and n > 0:
            if m == 1:
                ans += matrix[x][y:y+n]
                break
            if n == 1:
                ans += [matrix[x+i][y+n-1] for i in range(m)]
                break
            ans += matrix[x][y:y+n-1] + \
                   [matrix[x+i][y+n-1] for i in range(m-1)] + \
                   matrix[x+m-1][y+n-1:y:-1] + \
                   [matrix[x+i][y] for i in range(m-1, 0, -1)]
            x += 1
            y += 1
            m -= 2
            n -= 2

        return ans

t = Solution()
assert(t.spiralOrder([[1]]) == [1])
assert(t.spiralOrder([[1, 2], [3, 4]]) == [1, 2, 4, 3])
assert(t.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
print("tests passed")
