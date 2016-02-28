class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len, p_len = len(s), len(p)
        s_pointer, p_pointer = 0, 0
        star, s_star = -1, -1
        while s_pointer < s_len:
            if (p_pointer < p_len) and (s[s_pointer] == p[p_pointer] or p[p_pointer] == '?'):
                s_pointer += 1
                p_pointer += 1
                continue

            if (p_pointer < p_len) and (p[p_pointer] == '*'):
                star = p_pointer
                p_pointer += 1
                s_star = s_pointer
                continue

            if star >= 0:
                p_pointer = star + 1
                s_star += 1
                s_pointer = s_star
                continue

            return False

        while p_pointer < p_len and p[p_pointer] == '*':
            p_pointer += 1

        return p_pointer == p_len

t = Solution()
assert(t.isMatch('aa', '*'))
print("tests passed")
