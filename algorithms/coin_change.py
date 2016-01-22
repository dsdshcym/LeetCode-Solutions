class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        nums = [0,] + [-1,] * amount
        for i in range(1, amount + 1):
            pre = [nums[i - c]
                   for c in coins
                   if i - c >= 0 and nums[i - c] >= 0]
            if pre:
                nums[i] = (min(pre) + 1)
        return nums[amount]

t = Solution()
assert(t.coinChange([1, 2, 5], 11) == 3)
assert(t.coinChange([2,], 3) == -1)
print("tests passed")
