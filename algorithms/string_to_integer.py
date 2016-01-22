class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = str.strip()
        if not s:
            return str
        sign = 1
        if s[0] == '-':
            sign = -1
        if s[0] in '-+':
            s = s[1:]
        s = s.lstrip('0')
        ans = 0
        for c in s:
            if c in '0123456789':
                ans = ans * 10 + ord(c) - ord('0')
            else:
                break
        ans = sign * ans
        if ans > INT_MAX:
            ans = INT_MAX
        if ans < INT_MIN:
            ans = INT_MIN
        return ans

t = Solution()
assert(t.myAtoi("") == 0)
assert(t.myAtoi("  -0012a42") == -12)
assert(t.myAtoi("  -001111111111111111112a42") == -2147483648)
print("tests passed")
