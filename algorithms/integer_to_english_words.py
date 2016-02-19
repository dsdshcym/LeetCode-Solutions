class Solution(object):
    ONES_STRING = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
    ]

    TENS_STRING = [
        "",
        "",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]

    UNITS = [
        "Billion",
        "Million",
        "Thousand",
        "",
    ]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        slices = []
        for i in range(4):
            slices.append(num % 1000)
            num = num // 1000

        def three_bits_to_words(num):
            hundreds, tens, ones = num // 100, (num // 10) % 10, num % 10
            result = []
            if hundreds:
                result += [self.ONES_STRING[hundreds], "Hundred"]
            if tens == 1:
                result += [self.TENS_STRING[tens*10+ones]]
            else:
                result += [self.TENS_STRING[tens]]
                if ones:
                    result += [self.ONES_STRING[ones]]
            while "" in result:
                result.remove("")
            if result:
                return " ".join(result)
            else:
                return "Zero"

        results = list(map(three_bits_to_words, slices))
        ans = []
        for i, result in enumerate(results[::-1]):
            if result != "Zero":
                ans.append(result)
                if self.UNITS[i]:
                    ans.append(self.UNITS[i])
        if ans:
            return " ".join(ans)
        else:
            return "Zero"

t = Solution()
assert(t.numberToWords(0) == "Zero")
assert(t.numberToWords(20) == "Twenty")
assert(t.numberToWords(1000) == "One Thousand")
assert(t.numberToWords(123000123) == "One Hundred Twenty Three Million One Hundred Twenty Three")
assert(t.numberToWords(123) == "One Hundred Twenty Three")
assert(t.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five")
assert(t.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
print("tests passed")
