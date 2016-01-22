class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

t = Solution()
assert(t.strStr('123', '1') == 0)
print("tests passed")
