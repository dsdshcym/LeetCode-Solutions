class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            ans = int(str(x)[::-1])
        if x < 0:
            ans = int('-' + str(x)[1:][::-1])
        if ans >= 1 << 31 or ans < -(1 << 31):
            return 0
        return ans

def test_solution():
    t = Solution()
    assert t.reverse(123) == 321
    assert t.reverse(-123) == -321
    assert t.reverse(1534236469) == 0
