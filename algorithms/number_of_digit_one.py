class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, mask, r = 0, 1, 0
        while mask <= n:
            ans += n // (mask * 10) * mask
            current_bit = (n // mask) % 10
            if current_bit == 1:
                ans += (n % mask) + 1
            if current_bit > 1:
                ans += mask
            mask *= 10
        return ans

t = Solution()
assert(t.countDigitOne(0) == 0)
assert(t.countDigitOne(10) == 2)
assert(t.countDigitOne(13) == 6)
assert(t.countDigitOne(23) == 13)
print("tests passed")
