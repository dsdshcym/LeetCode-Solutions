class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** 0.5)

t = Solution()
# for i in range(1, 101):
#     print(t.bulbSwitch(i))
assert(t.bulbSwitch(3) == 1)
print("tests passed")
