class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

t = Solution()
assert t.isAnagram("anagram", "nagaram")
assert not t.isAnagram("rat", "cat")

print "tests passed"
