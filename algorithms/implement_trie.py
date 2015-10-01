from collections import defaultdict

class TrieNode(object):
    def __init__(self, char = ""):
        """
        Initialize your data structure here.
        """
        self.child = defaultdict(TrieNode)
        self.isLeaf = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            node = node.child[char]
        node.isLeaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            node = node.child.get(char)
            if not node:
                return False
        return node.isLeaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            node = node.child.get(char)
            if not node:
                return False
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
assert(trie.search("somestring"))
assert(trie.startsWith("some"))
assert(not trie.search("s"))
print "tests passed"
