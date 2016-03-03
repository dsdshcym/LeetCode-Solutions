class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            if i < 0:
                num_a = 0
            else:
                num_a = ord(a[i]) - ord('0')
                i -= 1

            if j < 0:
                num_b = 0
            else:
                num_b = ord(b[j]) - ord('0')
                j -= 1

            s = num_a + num_b + carry
            carry = s // 2
            ans.append(str(s % 2))

        if carry:
            ans.append(str(carry))

        return ''.join(ans[::-1])

t = Solution()
assert(t.addBinary('100', '1') == '101')
assert(t.addBinary('11', '1') == '100')
print("tests passed")
