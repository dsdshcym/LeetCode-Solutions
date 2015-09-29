class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        ans = ""
        D = 2 * numRows - 2
        N = len(s)
        for i in xrange(numRows):
            if (i < numRows - 1):
                delta = D - 2 * i
            else:
                delta = D
            j = i
            while (j < N):
                ans += s[j]
                j += delta
                if (D != delta):
                    delta = D - delta
        return ans

t = Solution()
assert(t.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
assert(t.convert("AB", 2) == "AB")
assert(t.convert("A", 1) == "A")
assert(t.convert("ABCDE", 4) == "ABCED")
print "tests passed"
