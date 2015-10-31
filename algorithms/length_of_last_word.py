class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = s.strip().split(' ')
        return len(strs[-1])

def test():
    t = Solution()

    assert t.lengthOfLastWord('Hello World') == 5
    assert t.lengthOfLastWord('a ') == 1
    assert t.lengthOfLastWord('') == 0
