class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'

        N = len(s)

        RL = [0,] * N
        center = max_right = 0
        max_half_len = ans_center = 0

        for i in range(N):
            if i < max_right:
                RL[i] = min(RL[2 * center - i], max_right - i)

            while i - (RL[i] + 1) >= 0 and \
                  i + (RL[i] + 1) < N and \
                  s[i - (RL[i] + 1)] == s[i + (RL[i] + 1)]:
                RL[i] += 1

            if RL[i] + i > max_right:
                max_right = RL[i] + i
                center = i

            if RL[i] > max_half_len:
                max_half_len = RL[i]
                ans_center = i

        result = s[ans_center-RL[ans_center]:ans_center+RL[ans_center]+1]

        return ''.join(result.split('#'))

t = Solution()
assert(t.longestPalindrome('abaaba') == 'abaaba')
print("tests passed")
