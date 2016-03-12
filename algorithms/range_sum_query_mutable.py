class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.bits = [sum(x
                         for x in nums[i - self.lowbit(i) + 1:i + 1])
                     for i in range(len(nums))]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if i == 0:
            self.nums[0] = val
            return
        n = len(self.nums)
        delta = val - self.nums[i]
        self.nums[i] = val
        j = i
        while j < n:
            self.bits[j] += delta
            j += self.lowbit(j)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        sum_i, sum_j = 0, self.nums[i]
        while i > 0:
            sum_i += self.bits[i]
            i -= self.lowbit(i)
        while j > 0:
            sum_j += self.bits[j]
            j -= self.lowbit(j)
        return sum_j - sum_i

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
