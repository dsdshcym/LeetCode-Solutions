class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        N = len(prices)
        ans = 0
        first_profit = [0,] * len(prices)
        min_price = prices[0]
        for i in range(1, N):
            first_profit[i] = max(first_profit[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])

        max_price = prices[-1]
        profit = 0
        for i in range(N - 1, -1, -1):
            profit = max(profit, max_price - prices[i])
            max_price = max(max_price, prices[i])
            ans = max(ans, profit + first_profit[i])

        return ans
