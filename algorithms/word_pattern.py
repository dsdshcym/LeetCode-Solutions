class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        hash_word_char = {}
        hash_char_word = {}
        for (char, word) in zip(pattern, words):
            hash_word_char.setdefault(word, char)
            if hash_word_char[word] != char:
                return False
            hash_char_word.setdefault(char, word)
            if hash_char_word[char] != word:
                return False
        return True

t = Solution()
assert t.wordPattern("abba", "dog cat cat dog")
assert not t.wordPattern("aaaa", "dog cat cat dog")
assert not t.wordPattern("abba", "dog dog dog dog")
assert not t.wordPattern("abba", "dog cat cat fish")
assert not t.wordPattern("aaa", "aa aa aa aa")
print("tests passed")
