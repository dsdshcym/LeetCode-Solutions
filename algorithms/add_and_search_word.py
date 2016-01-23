from collections import defaultdict

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dictionary = defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.dictionary[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.dictionary[len(word)]
        else:
            for saved_word in self.dictionary[len(word)]:
                for i, c in enumerate(saved_word):
                    if c != word[i] and word[i] != '.':
                        break
                else:
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("word")
assert(wordDictionary.search("word"))
assert(not wordDictionary.search("pattern"))

wordDictionary.addWord("at")
wordDictionary.addWord("and")
wordDictionary.addWord("an")
wordDictionary.addWord("add")
wordDictionary.search("a")
wordDictionary.search(".at")
wordDictionary.addWord("bat")
wordDictionary.search(".at")
wordDictionary.search("an.")
wordDictionary.search("a.d.")
wordDictionary.search("b.")
wordDictionary.search("a.d")
wordDictionary.search(".")

print("tests passed")
