class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

t = Solution()

assert t.hammingWeight(11) == 3

print "tests passed"
