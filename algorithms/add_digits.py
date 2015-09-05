class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        # https://en.wikipedia.org/wiki/Digital_root
        return 1 + (num - 1) % 9 if num > 0 else 0

        while len(str(num)) > 1:
            num = sum([int(x) for x in str(num)])
        return num
