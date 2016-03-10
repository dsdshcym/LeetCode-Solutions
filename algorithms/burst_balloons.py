class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def max_coins_helper(left, right):
            if right - left <= 1:
                return 0
            if dp[left][right]:
                return dp[left][right]
            result = 0
            l, r = nums[left], nums[right]
            for i in range(left + 1, right):
                result = max(result,
                             l * nums[i] * r + \
                             max_coins_helper(left, i) + \
                             max_coins_helper(i, right))
            dp[left][right] = result
            return result

        return max_coins_helper(0, n - 1)

t = Solution()
print(t.maxCoins([3, 1, 5, 8]))
assert(t.maxCoins([3, 1, 5, 8]) == 167)
print("tests passed")
