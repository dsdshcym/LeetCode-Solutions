#+TAG: NEEDS_REWRITE
class Solution(object):
    def dfs(self, position, word):
        if word == "":
            return True
        for move in self.moves:
            new_position = [position[0] + move[0], position[1] + move[1]]
            if new_position[0] in range(self.N) and new_position[1] in range(self.M):
                if (not self.visited[new_position[0]][new_position[1]]) and \
                   (self.board[new_position[0]][new_position[1]] == word[0]):
                    self.visited[new_position[0]][new_position[1]] = True
                    if self.dfs(new_position, word[1:]):
                        return True
                    self.visited[new_position[0]][new_position[1]] = False
        return False

    def findWordInBoard(self, word):
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == word[0]:
                    if self.dfs([i, j], word[1:]):
                        return True
        return False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.N = len(board)
        if self.N == 0:
            return False
        self.M = len(board[0])
        if self.M == 0:
            return False
        self.board = board
        self.moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = []
        for word in words:
            self.visited = [[False for _ in range(self.M)] for _ in range(self.N)]
            if self.findWordInBoard(word):
                ans.append(word)
        return ans

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
assert(t.findWords(board, words) == ans)
assert(t.findWords(["a"], ["a"]) == ["a"])
