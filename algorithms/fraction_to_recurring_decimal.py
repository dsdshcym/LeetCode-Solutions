class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if (numerator == 0):
            return '0'
        ans = str()
        if (numerator < 0) ^ (denominator < 0):
            ans = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        ans += str(numerator / denominator)
        remain = numerator % denominator
        if (remain == 0):
            return ans
        remain_pos = {remain: 0}
        frac = ''
        i = 0
        while True:
            i += 1
            new_frac = remain * 10 / denominator
            frac += str(new_frac)
            remain = remain * 10 % denominator

            if (remain == 0):
                ans = ans + '.' + frac
                break

            if (remain in remain_pos.keys()):
                ans = ans + '.' + frac[:remain_pos[remain]] + '(' + frac[remain_pos[remain]:] + ')'
                break
            else:
                remain_pos[remain] = i

        return ans

t = Solution()
assert(t.fractionToDecimal(2, 1) == '2')
assert(t.fractionToDecimal(1, 2) == '0.5')
assert(t.fractionToDecimal(2, 3) == '0.(6)')
assert(t.fractionToDecimal(1, 6) == '0.1(6)')
assert(t.fractionToDecimal(-50, 8) == '-6.25')
assert(t.fractionToDecimal(0, -5) == '0')
print('test passed')
