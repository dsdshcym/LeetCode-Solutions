class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        count = 1
        while count < n:
            count += 1
            N = len(num)
            i = 0
            s = 1
            new_num = ''
            while i < N:
                while i < N - 1 and num[i] == num[i+1]:
                    i += 1
                    s += 1
                new_num += str(s) + num[i]
                i += 1
                s = 1
            num = new_num
        return num

t = Solution()
assert(t.countAndSay(1) == '1')
assert(t.countAndSay(2) == '11')
assert(t.countAndSay(3) == '21')
assert(t.countAndSay(4) == '1211')
assert(t.countAndSay(5) == '111221')
assert(t.countAndSay(6) == '312211')
assert(t.countAndSay(7) == '13112221')
print("tests passed")
