class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i > 0:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]

        nums[i:] = nums[i:][::-1]

t = Solution()
a = [1, 2, 3]
t.nextPermutation(a)
assert(a == [1, 3, 2])
b = [1]
t.nextPermutation(b)
assert(b == [1])
print("tests passed")
