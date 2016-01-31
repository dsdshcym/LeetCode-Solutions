class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(x, nums):
            l, r = 0, len(nums)
            while l < r - 1:
                mid = (l + r) >> 1
                if nums[mid] > x:
                    r = mid
                else:
                    l = mid
            return x == nums[l]

        for row in matrix:
            if target > row[-1]:
                continue
            if target < row[0]:
                break
            if binary_search(target, row):
                return True
        return False

t = Solution()
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
assert(t.searchMatrix(matrix, 5))
assert(not t.searchMatrix(matrix, 20))
assert(t.searchMatrix([[-1, 3]], 3))
print("tests passed")
