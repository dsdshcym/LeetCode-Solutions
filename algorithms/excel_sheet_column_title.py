class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:
            offset = (n % 26)
            if not offset:
                offset = 26
                n = n // 26 - 1
            else:
                n //= 26
            ans = chr(ord('A') + offset - 1) + ans
        print(ans)
        return ans

t = Solution()
assert(t.convertToTitle(1) == 'A')
assert(t.convertToTitle(2) == 'B')
assert(t.convertToTitle(3) == 'C')
assert(t.convertToTitle(26) == 'Z')
assert(t.convertToTitle(27) == 'AA')
assert(t.convertToTitle(28) == 'AB')
assert(t.convertToTitle(29) == 'AC')
print("tests passed")
