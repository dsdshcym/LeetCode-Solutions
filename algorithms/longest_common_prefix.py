class Solution(object):
    def prefix(self, a, b):
        for i in xrange(min(len(a), len(b))):
            if b.find(a[:i + 1]) != 0:
                return a[:i]
        return a if len(a) < len(b) else b

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        return reduce(self.prefix, strs)

t = Solution()

assert t.longestCommonPrefix([]) == ''
assert t.longestCommonPrefix(['']) == ''
assert t.longestCommonPrefix(['', '']) == ''
assert t.longestCommonPrefix(['a', 'b']) == ''
assert t.longestCommonPrefix(['a', 'ab']) == 'a'

print "tests passed"
