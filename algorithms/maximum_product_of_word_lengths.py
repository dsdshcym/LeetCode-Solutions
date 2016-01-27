class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        char_bit = {}
        for word in words:
            bit = 0
            for char in word:
                bit |= 1 << (ord(char) - ord('A'))
            char_bit.setdefault(bit, len(word))
            char_bit[bit] = max(char_bit[bit], len(word))
        ans = 0
        for a in char_bit:
            for b in char_bit:
                if not a & b:
                    ans = max(ans, char_bit[a] * char_bit[b])
        return ans

t = Solution()
assert(t.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16)
assert(t.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4)
assert(t.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0)
print("tests passed")
