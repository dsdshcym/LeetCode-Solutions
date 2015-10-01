from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = defaultdict(TrieNode)
        self.isLeaf = False

class Trie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

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

class Solution(object):
    def dfs(self, x, y, word, node):
        if (x < 0) or (x >= self.N) or \
           (y < 0) or (y >= self.M) \
           or (self.visited[x][y]):
            return
        word = word + self.board[x][y]
        node = node.child.get(self.board[x][y])
        if not node:
            return
        if node.isLeaf:
            self.ans.add(word)
        self.visited[x][y] = True
        for move in self.moves:
            self.dfs(x + move[0], y + move[1], word, node)
        self.visited[x][y] = False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.ans = set()
        self.trie = Trie(words)
        self.board = board
        self.N = len(board)
        self.M = len(board[0])
        self.visited = [[False for _ in xrange(self.M)] for _ in xrange(self.N)]
        for i in xrange(self.N):
            for j in xrange(self.M):
                char = self.board[i][j]
                node = self.trie.root
                self.dfs(i, j, "", node)
        return list(self.ans)

t = Solution()
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath", "pea", "eat", "rain"]
ans = ["oath", "eat"]

print t.findWords(board, words)
print t.findWords(["a"], ["a"])
assert(set(t.findWords(board, words)) == set(ans))
assert(t.findWords(["a"], ["a"]) == ["a"])
print "test passed"
