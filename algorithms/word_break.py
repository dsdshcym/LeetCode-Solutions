class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        false_set = set()

        word_lens = set(map(len, wordDict))

        def check(s):
            if s in wordDict:
                return True
            if s in false_set:
                return False
            for i in word_lens:
                if s[:i] in wordDict:
                    if check(s[i:]):
                        return True
            false_set.add(s)
            return False

        return check(s)
