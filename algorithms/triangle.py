from sys import maxint

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        N = len(triangle)
        min_sum = []
        def get_min_sum(x, y):
            if x < 0 or x >= N or y < 0 or y >= len(min_sum[x]):
                return maxint
            return min_sum[x][y]
        for i, row in enumerate(triangle):
            if min_sum:
                min_sum.append([0,] * len(row))
                for j, num in enumerate(row):
                    min_sum[i][j] = min(get_min_sum(i-1, j-1), get_min_sum(i-1, j)) + num
            else:
                min_sum.append(list(row))
        return min(min_sum[N-1])

t = Solution()
test_case = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print(t.minimumTotal(test_case))
assert(t.minimumTotal(test_case) == 11)
