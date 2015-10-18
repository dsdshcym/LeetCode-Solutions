class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        ans = 0
        for c in s:
            if c not in sub:
                sub += c
                if len(sub) > ans:
                    ans = len(sub)
            else:
                pos = sub.find(c)
                sub = sub[pos + 1:] + c
        return ans

t = Solution()

assert t.lengthOfLongestSubstring('') == 0
assert t.lengthOfLongestSubstring('bbbb') == 1
assert t.lengthOfLongestSubstring('abcabcbb') == 3

print "tests passed"
