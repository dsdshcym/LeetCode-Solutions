class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] == 0:
                for j in xrange(i, N - 1):
                    nums[j] = nums[j + 1]
                nums[N - 1] = 0
                N -= 1
            else:
                i += 1

t = Solution()
nums = [0, 1, 0, 3, 1]
t.moveZeroes(nums)
assert nums == [1, 3, 1, 0, 0]
nums = [0, 0, 1]
t.moveZeroes(nums)
assert nums == [1, 0, 0]
print "tests passed"
