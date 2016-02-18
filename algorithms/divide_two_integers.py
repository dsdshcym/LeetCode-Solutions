MAX_INT = 2147483647

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        products = [divisor]
        twos_power = [1]
        while products[-1] < dividend:
            products.append(products[-1] + products[-1])
            twos_power.append(twos_power[-1] + twos_power[-1])
        ans = 0
        for power, product in list(zip(twos_power, products))[::-1]:
            if dividend <= 0:
                break
            if dividend >= product:
                ans += power
                dividend -= product
        if ans > MAX_INT and sign != -1:
            return MAX_INT
        else:
            return sign * ans

t = Solution()
assert(t.divide(1, 2) == 0)
assert(t.divide(-2, 1) == -2)
assert(t.divide(2, 1) == 2)
assert(t.divide(3, 1) == 3)
assert(t.divide(30, 2) == 15)
print("tests passed")
