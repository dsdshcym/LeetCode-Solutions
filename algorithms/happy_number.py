class Solution(object):
    def __init__(self):
        self.appeared = []

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n in self.appeared:
            return False
        self.appeared.append(n)

        n_s = str(n)
        t = 0
        for c in n_s:
            t += (ord(c) - ord('0')) ** 2
        return self.isHappy(t)

t = Solution()

assert t.isHappy(1)
assert t.isHappy(82)
assert t.isHappy(68)
assert t.isHappy(10)
assert not t.isHappy(2)

print("tests passed")
