class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if row[0] > target:
                return False
            if row[-1] >= target:
                if target in row:
                    return True
        return False

m = [[1,   3,  5,  7],
     [10, 11, 16, 20],
     [23, 30, 34, 50]]

assert Solution().searchMatrix(m, 3)

print("tests passed")
