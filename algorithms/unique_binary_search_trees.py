class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        return self.numTrees(n - 1) * (4 * n - 2) / (n + 1)

        # f = [1, 1]
        # for i in xrange(2, n + 1):
        #     f.append(sum([f[i - 1 - j] * f[j] for j in xrange(i)]))
        # return f[n]

t = Solution()

assert t.numTrees(1) == 1
assert t.numTrees(2) == 2
assert t.numTrees(3) == 5

for i in xrange(10):
    print t.numTrees(i)
