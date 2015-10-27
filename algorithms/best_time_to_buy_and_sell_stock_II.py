class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in xrange(len(prices) - 1):
            delta = prices[i + 1] - prices[i]
            if delta > 0:
                ans += delta
        return ans
