class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = 0
        for num in nums:
            if num != 0:
                nums[p] = num
                p += 1
        for i in xrange(p, len(nums)):
            nums[i] = 0

t = Solution()
nums = [0, 1, 0, 3, 1]
t.moveZeroes(nums)
assert nums == [1, 3, 1, 0, 0]
nums = [0, 0, 1]
t.moveZeroes(nums)
assert nums == [1, 0, 0]
print "tests passed"
