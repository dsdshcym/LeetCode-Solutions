class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_price = prices[0]
        ans = 0
        for price in prices:
            ans = max(price - min_price, ans)
            min_price = min(price, min_price)
        return ans

t = Solution()

assert t.maxProfit([1, 3, 2, 3]) == 2
assert t.maxProfit([]) == 0

print "tests passed"
