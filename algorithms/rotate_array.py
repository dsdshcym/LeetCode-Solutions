class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        temp_list = list(nums)
        for i in range(N):
            nums[i] = temp_list[(N - k + i) % N]

nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4]
