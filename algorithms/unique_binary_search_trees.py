class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [1, 1]
        for i in xrange(2, n + 1):
            f.append(sum([f[i - 1 - j] * f[j] for j in xrange(i)]))
        return f[n]

t = Solution()

assert t.numTrees(1) == 1
assert t.numTrees(2) == 2
assert t.numTrees(3) == 5
