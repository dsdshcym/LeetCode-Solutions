class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        f = [[i+j for j in range(len2 + 1)] for i in range(len1 + 1)]

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                f[i][j] = min(f[i - 1][j - 1],
                                f[i - 1][j],
                                f[i][j - 1]) + (word1[i - 1] != word2[j - 1])

        return f[len1][len2]

t = Solution()
assert(t.minDistance("sea", "eat") == 2)
print("tests passed")
