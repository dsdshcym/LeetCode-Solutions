class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(N-1):
            for j in range(i, N):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

        # This can not work
        # Since it will create a new list
        # So it's not modifying in-place
        # nums = [0 for _ in xrange(nums.count(0))] + \
        #        [1 for _ in xrange(nums.count(1))] + \
        #        [2 for _ in xrange(nums.count(2))]
