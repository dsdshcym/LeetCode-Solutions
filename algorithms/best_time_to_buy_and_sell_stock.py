class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_price = [0]
        for i, price in enumerate(prices[::-1]):
            max_price.append(max(max_price[i], price))
        max_price = max_price[1::][::-1]
        return max((max_price[i] - prices[i] for i in xrange(len(prices))))

t = Solution()

assert t.maxProfit([1, 3, 2, 3]) == 2
assert t.maxProfit([]) == 0

print "tests passed"
