class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]

t = Solution()
assert(t.addBinary('100', '1') == '101')
assert(t.addBinary('11', '1') == '100')
print("tests passed")
