class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_appear = {c: i for i, c in enumerate(s)}
        ans = []
        for i, c in enumerate(s):
            if c not in ans:
                while ans and c < ans[-1] and i < last_appear[ans[-1]]:
                    ans.pop(-1)
                ans.append(c)
        return ''.join(ans)

t = Solution()
assert(t.removeDuplicateLetters('bcabc') == 'abc')
assert(t.removeDuplicateLetters('cbacdcbc') == 'acdb')
print("tests passed")
