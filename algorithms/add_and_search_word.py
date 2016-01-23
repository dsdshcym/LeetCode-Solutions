class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.ended = False
        self.children = {}

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode(c))
        node.ended = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        queue = [(self.root, word)]
        while queue:
            node, remain = queue.pop(0)
            if not remain:
                if node.ended:
                    return True
                else:
                    continue
            next_char = remain[0]
            remain = remain[1:]
            if next_char == '.':
                queue += [(child, remain) for child in node.children.values()]
            elif next_char in node.children:
                queue.append((node.children[next_char], remain))
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
