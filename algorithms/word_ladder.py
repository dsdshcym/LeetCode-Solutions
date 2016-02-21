class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Two-End BFS
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        N = len(beginWord)
        wordList.add(endWord)
        queue = [beginWord, endWord]
        visited = {beginWord: 1, endWord: -1}
        while queue:
            word = queue.pop(0)
            h = visited[word]
            for i in range(N):
                for char in string.ascii_lowercase:
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in wordList:
                        if next_word not in visited:
                            queue.append(next_word)
                            visited[next_word] = h + 1 if h > 0 else h - 1
                        elif (visited[next_word] > 0) ^ (h > 0):
                            return abs(h - visited[next_word])
        return 0

t = Solution()
assert(t.ladderLength("hit", "cog", {"hot","dot","dog","lot","log"}) == 5)
print("tests passed")
