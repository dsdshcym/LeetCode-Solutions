#+TAG: NEEDS_REWRITE
class TrieNode():
    def __init__(self, char, brother = None, child = None):
        self.char = char
        self.brother = brother
        self.child = child
        self.isLeaf = self.child != None

    def setIsLeaf(self):
        self.isLeaf = True

    def setBrother(self, brother):
        self.brother = brother

    def setChild(self, child):
        self.child = child

    def getChar(self):
        return self.char

    def getBrother(self):
        return self.brother

    def getChild(self):
        return self.child

class Trie():
    def __init__(self, words):
        self.root = TrieNode("")
        for word in words:
            self.insertWord(word)

    def insertWord(self, word):
        pre_node = self.root
        while word != "":
            node = pre_node.getChild()
            if not node:
                node = TrieNode(word[0])
                pre_node.setChild(node)
                word = word[1:]
                break
            while node and (node.getChar() != word[0]):
                pre_node = node
                node = node.getBrother()
            if (node == None):
                node = TrieNode(word[0])
                pre_node.setBrother(node)
                word = word[1:]
                break
        while word != "":
            pre_node = node
            node = TrieNode(word[0])
            pre_node.setChild(node)
            word = word[1:]
        node.setIsLeaf()

    def findWord(self, word):
        node = self.root
        while node and (word != ""):
            node = node.getChild()
            if not node:
                break
            while node.getChar() != word[0]:
                node = node.getBrother()
                if not node:
                    break
            if (node) and (node.isLeaf) and (len(word) == 1):
                return 2
            word = word[1:]
        return 0 if word else 1

class Solution(object):
    def dfs(self, x, y, word):
        if (x not in xrange(self.N)) \
           or (y not in xrange(self.M)) \
           or (self.visited[x][y]):
            return
        word = word + self.board[x][y]
        result = self.trie.findWord(word)
        if result == 0:
            return
        if result == 2:
            self.ans.append(word)
        self.visited[x][y] = True
        for move in self.moves:
            self.dfs(x + move[0], y + move[1], word)
        self.visited[x][y] = False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.ans = []
        self.trie = Trie(words)
        self.board = board
        self.N = len(board)
        self.M = len(board[0])
        self.visited = [[False for _ in xrange(self.M)] for _ in xrange(self.N)]
        for i in xrange(self.N):
            for j in xrange(self.M):
                self.dfs(i, j, "")
        return self.ans

t = Solution()
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath", "pea", "eat", "rain"]
ans = ["oath", "eat"]

# print t.findWords(board, words)
# print t.findWords(["a"], ["a"])
# assert(set(t.findWords(board, words)) == set(ans))
assert(t.findWords(["a"], ["a"]) == ["a"])
print "test passed"
