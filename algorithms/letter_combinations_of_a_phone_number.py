class Solution(object):
    DIGIT_TO_CHAR = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []

        for digit in digits:
            ans = [pre + c
                   for pre in ans or ['']
                   for c in self.DIGIT_TO_CHAR.get(digit, '')]

        return ans
