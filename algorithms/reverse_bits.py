class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = bin(n)[2:]
        return int(b[::-1] + '0' * (32 - len(b)), 2)

def test_solution():
    t = Solution()
    assert t.reverseBits(43261596) == 964176192
