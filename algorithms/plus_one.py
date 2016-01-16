class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        r = 1
        for i in range(N - 1, -1, -1):
            s = r + digits[i]
            digits[i] = s % 10
            r = s // 10
            if r == 0:
                break
        if r > 0:
            digits.insert(0, r)
        return digits

t = Solution()
assert t.plusOne([1, 0, 0]) == [1, 0, 1]
assert t.plusOne([1, 9, 9]) == [2, 0, 0]
assert t.plusOne([9, 9]) == [1, 0, 0]
print("tests passed")
