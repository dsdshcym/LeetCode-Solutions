class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        ans = ''
        for i in xrange(len(strs[0])):
            tmp = strs[0][:i + 1]
            for s in strs:
                if s[:i + 1] != tmp:
                    return strs[0][:i]
        return strs[0]

t = Solution()

assert t.longestCommonPrefix([]) == ''
assert t.longestCommonPrefix(['', '']) == ''
assert t.longestCommonPrefix(['a', 'b']) == ''
assert t.longestCommonPrefix(['a', 'ab']) == 'a'

print "tests passed"
