class Solution(object):
    def check(self, a, b, num):
        if not a or not b or \
           (len(a) > 1 and a[0] == '0') or \
           (len(b) > 1 and b[0] == '0'):
            return False
        if not num:
            return True
        s = str(int(a) + int(b))
        if num.startswith(s):
            return self.check(b, s, num[len(s):])
        return False

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return any(self.check(num[:i+1], num[i+1:j+1], num[j+1:])
                   for i in range(len(num)-2)
                   for j in range(i+1, len(num)-1))

t = Solution()
assert(t.isAdditiveNumber("112358"))
assert(t.isAdditiveNumber("199100199"))
assert(t.isAdditiveNumber("101"))
assert(not t.isAdditiveNumber("1023"))
print("tests passed")
