class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        nums = [0] + nums
        self.bits = [sum(x
                         for x in nums[i - self.lowbit(i) + 1:i + 1])
                     for i in range(len(nums))]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        n = len(self.bits)
        delta = val - self.sumRange(i, i)
        i += 1
        while i < n:
            self.bits[i] += delta
            i += self.lowbit(i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        result = 0
        j += 1
        while i != j:
            if i < j:
                result += self.bits[j]
                j -= self.lowbit(j)
            else:
                result -= self.bits[i]
                i -= self.lowbit(i)
        return result

    def lowbit(self, x):
        return x & (-x)

# Your NumArray object will be instantiated and called as such:
nums = [9,-8]
num_array = NumArray(nums)
num_array.update(0,3)
assert(num_array.sumRange(1,1) == -8)
assert(num_array.sumRange(0,1) == -5)
num_array.update(1,-3)
assert(num_array.sumRange(0,1) == 0)
print("tests passed")
