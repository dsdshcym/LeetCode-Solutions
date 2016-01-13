class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        NUMS = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and NUMS[s[i]] < NUMS[s[i + 1]]:
                ans -= NUMS[s[i]]
            else:
                ans += NUMS[s[i]]
        return ans

t = Solution()
assert t.romanToInt('I') == 1
assert t.romanToInt('MCMXC') == 1990
assert t.romanToInt('MMXIV') == 2014
assert t.romanToInt('MCMLIV') == 1954

print("test passed")
