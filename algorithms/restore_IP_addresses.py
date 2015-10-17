class Solution(object):
    def judge(self, s):
        if len(s) > 1 and s[0] == '0':
            return False
        return s != '' and 0 <= int(s) <= 255

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        r = xrange(1, 4)
        ans = []
        for i in r:
            a = s[: i]
            if not self.judge(a):
                break
            for j in r:
                b = s[i: i + j]
                if not self.judge(b):
                    break
                for k in r:
                    c = s[i + j: i + j + k]
                    if not self.judge(c):
                        break
                    d = s[i + j + k:]
                    if not self.judge(d):
                        continue
                    ans.append('.'.join([a, b, c, d]))
        return ans

t = Solution()

assert(t.restoreIpAddresses('1111') == ['1.1.1.1'])
assert(t.restoreIpAddresses('25525511135') == ["255.255.11.135", "255.255.111.35"])
assert(t.restoreIpAddresses('010010') == ["0.10.0.10","0.100.1.0"])

print "tests passed"
