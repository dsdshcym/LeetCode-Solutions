class Solution(object):
    MOVE = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            if word == "":
                return True
            return False

        N, M = len(board), len(board[0])
        visited = [[False,] * M for i in range(N)]

        def dfs(x, y, index):
            if index >= len(word):
                return True
            if x < 0 or x >= N or y < 0 or y >= M or visited[x][y]:
                return False
            if board[x][y] != word[index]:
                return False
            visited[x][y] = True
            for move_x, move_y in self.MOVE:
                new_x, new_y = x + move_x, y + move_y
                if dfs(new_x, new_y, index + 1):
                    return True
            visited[x][y] = False
            return False

        for i in range(N):
            for j in range(M):
                if dfs(i, j, 0):
                    return True
        return False

t = Solution()
board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
word = "oath"
assert(t.exist(board, word))

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"
assert(t.exist(board, word))
word = "SEE"
assert(t.exist(board, word))
word = "ABCB"
assert(not t.exist(board, word))

print("tests passed")
