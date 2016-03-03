from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lens, lent = len(s), len(t)
        if lens < lent:
            return ""

        target_count = defaultdict(int)
        source_count = defaultdict(int)

        for char in t:
            target_count[char] += 1

        current_start = min_start = 0
        min_len = lens + 1
        remain = lent

        for end, char in enumerate(s):
            source_count[char] += 1
            if target_count[char] >= source_count[char] > 0:
                remain -= 1
            if remain == 0:
                first_char = s[current_start]
                while source_count[first_char] > target_count[first_char]:
                    source_count[first_char] -= 1
                    current_start += 1
                    first_char = s[current_start]
                if end - current_start + 1 < min_len:
                    min_len = end - current_start + 1
                    min_start = current_start

        if min_len <= lens:
            return s[min_start: min_start + min_len]
        else:
            return ""

t = Solution()
print(t.minWindow("ADOBECODEBANC", "ABC"))
assert(t.minWindow("ADOBECODEBANC", "ABC") == "BANC")
print("tests passed")
