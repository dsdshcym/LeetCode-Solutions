class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s_t = {}
        map_t_s = {}
        for i, c in enumerate(s):
            map_t_s.setdefault(t[i], c)
            if map_t_s[t[i]] != c:
                return False
            map_s_t.setdefault(c, t[i])
            if map_s_t[c] != t[i]:
                return False
        return True

t = Solution()
assert t.isIsomorphic('egg', 'add')
assert t.isIsomorphic('paper', 'title')
assert not t.isIsomorphic('aaaa', 'bccb')
assert not t.isIsomorphic('foo', 'bar')
print("tests passed")
