class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count = {}
        A = B = 0
        matched = [False for i in range(len(guess))]
        for char in secret:
            count.setdefault(char, 0)
            count[char] += 1
        for i, char in enumerate(guess):
            if char == secret[i]:
                matched[i] = True
                count[char] -= 1
                A += 1
        for i, char in enumerate(guess):
            if matched[i]:
                continue
            if count.setdefault(char, 0) > 0:
                count[char] -= 1
                B += 1
        return "%iA%iB" % (A, B)

t = Solution()
assert(t.getHint("1807", "7810") == "1A3B")
assert(t.getHint("1123", "0111") == "1A1B")
assert(t.getHint("0110", "1123") == "1A1B")
assert(t.getHint("11", "10") == "1A0B")
print("tests passed")
