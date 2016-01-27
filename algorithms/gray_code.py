class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        tmp = self.grayCode(n-1)
        return tmp + [(1 << (n-1)) + x for x in tmp[::-1]]

t = Solution()
assert(t.grayCode(2) == [0, 1, 3, 2])
assert(t.grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4])
print("tests passed")
