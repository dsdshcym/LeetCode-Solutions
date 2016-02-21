class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        BITS = 9
        MASK = 10 ** BITS

        def str_to_bits_list(num):
            num = num[::-1]
            return [int(num[BITS*i:BITS*i+BITS][::-1])
                    for i in range(len(num)//BITS+int(len(num)%BITS>0))]

        l1 = str_to_bits_list(num1)
        l2 = str_to_bits_list(num2)
        l3 = [0,] * (len(l1) + len(l2))

        for i in range(len(l1)):
            for j in range(len(l2)):
                m = l1[i] * l2[j]
                l3[i + j] += m
                k = i + j
                r = l3[k] // MASK
                while r:
                    l3[k] %= MASK
                    k += 1
                    l3[k] += r
                    r = l3[k] // MASK

        ans = ''.join(map(lambda x: "0" * (BITS - len(str(x))) + str(x)
                          , l3[::-1])).lstrip("0")
        if ans:
            return ans
        else:
            return "0"

t = Solution()
assert(t.multiply("0", "0") == str(0))
assert(t.multiply("1", "4") == str(1 * 4))
assert(t.multiply("5", "4") == str(5 * 4))
assert(t.multiply("5000", "4001") == str(5000 * 4001))
assert(t.multiply("12345678", "56781234") == str(12345678 * 56781234))
assert(t.multiply("123456789", "987654321") == str(123456789 * 987654321))
print("tests passed")
