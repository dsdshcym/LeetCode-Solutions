class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        N = len(nums)
        self.s = [0, ] * N
        for i, num in enumerate(nums):
            self.s[i] = num
            if i > 0:
                self.s[i] += self.s[i-1]
        self.nums = nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j] - self.s[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

nums = [-2, 0, 3, -5, 2, -1]
t = NumArray(nums)
assert(t.sumRange(0, 2) == 1)
assert(t.sumRange(1, 2) == 3)
print("tests passed")
