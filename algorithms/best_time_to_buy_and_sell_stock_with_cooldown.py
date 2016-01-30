from sys import maxint

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INTMIN = -maxint - 1
        hold, not_hold, not_hold_cooldown = INTMIN, 0, INTMIN
        for price in prices:
            hold, not_hold, not_hold_cooldown = max(hold, not_hold - price), max(not_hold, not_hold_cooldown), hold + price
        return max(not_hold_cooldown, not_hold)

t = Solution()
assert(t.maxProfit([]) == 0)
assert(t.maxProfit([1, 2, 3, 0, 2]) == 3)
assert(t.maxProfit([3, 2, 1, 0, 2]) == 2)
assert(t.maxProfit([3, 2, 1]) == 0)
print("tests passed")
