class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            begin = right
        else:
            begin = -1
        if nums[left] == target:
            begin = left
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            end = left
        else:
            end = -1
        if nums[right] == target:
            end = right
        return [begin, end]

assert Solution().searchRange([1,], 0) == [-1, -1]
assert Solution().searchRange([1, 3], 1) == [0, 0]
assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
print("tests passed")
