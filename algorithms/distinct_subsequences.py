class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or len(s) < len(t):
            return 0
        f = [1] + [0 for j in xrange(len(t))]

        for i, si in enumerate(s):
            for j, tj in reversed(list(enumerate(t))):
                f[j + 1] = f[j + 1] + (f[j] * (si == tj))

        return f[len(t)]

        # f = [[0 for j in xrange(len(t) + 1)] for i in xrange(len(s) + 1)]

        # for i, si in enumerate(s):
        #     f[i][0] = 1
        #     for j, tj in enumerate(t):
        #         f[i + 1][j + 1] = f[i][j + 1] + (f[i][j] * (si == tj))

        # return f[len(s)][len(t)]
