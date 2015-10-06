class Solution(object):
    def compare(self, s1, s2):
        v1 = int(s1)
        v2 = int(s2)
        if v1 > v2:
            return 1
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in xrange(max(len(v1), len(v2))):
            if i >= len(v1):
                v1.append('0')
            if i >= len(v2):
                v2.append('0')
            compare_result = self.compare(v1[i], v2[i])
            if compare_result != 0:
                return compare_result
        return 0

t = Solution()

assert(t.compareVersion('0.1', '1.1') == -1)
assert(t.compareVersion('0.1', '0.1') == 0)
assert(t.compareVersion('0.100', '0.1') == 1)
assert(t.compareVersion('13.1', '1.1') == 1)
assert(t.compareVersion('01', '1') == 0)
assert(t.compareVersion('01', '1.0') == 0)
assert(t.compareVersion('01.0.1', '1.0') == 1)

print "tests passed"
