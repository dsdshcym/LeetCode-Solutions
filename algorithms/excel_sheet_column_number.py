class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for c in s:
            ans *= 26
            ans += ord(c) - ord('A') + 1
        return ans

t = Solution()

assert t.titleToNumber('A') == 1
assert t.titleToNumber('B') == 2
assert t.titleToNumber('C') == 3
assert t.titleToNumber('D') == 4
assert t.titleToNumber('E') == 5

assert t.titleToNumber('AA') == 27
assert t.titleToNumber('AB') == 28
assert t.titleToNumber('AC') == 29
assert t.titleToNumber('AD') == 30
assert t.titleToNumber('AE') == 31

print("tests passed")
