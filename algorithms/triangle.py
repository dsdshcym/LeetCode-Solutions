class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)
        min_sum = triangle[-1]
        for row in triangle[-2::-1]:
            for j, num in enumerate(row):
                min_sum[j] = min(min_sum[j+1], min_sum[j]) + row[j]
        return min_sum[0]

t = Solution()
test_case = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
assert(t.minimumTotal(test_case) == 11)
print("tests passed")
