class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        ways = [1, 1]
        for i in range(1, len(s)):
            temp = 0
            if 1 <= int(s[i]) <= 9:
                temp += ways[-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += ways[-2]
            ways.append(temp)
        return ways[-1]

t = Solution()
assert(t.numDecodings('0') == 0)
assert(t.numDecodings('10001') == 0)
assert(t.numDecodings('1010') == 1)
assert(t.numDecodings('12') == 2)
assert(t.numDecodings('22') == 2)
assert(t.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"))
print("tests passed")
