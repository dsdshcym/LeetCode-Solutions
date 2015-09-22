class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = (left + right) / 2
            if (nums[mid] == target):
                return mid
            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] >= target:
            return left
        else:
            return left + 1

t = Solution()
assert t.searchInsert([1,3,5,6], 5) == 2
assert t.searchInsert([1,3,5,6], 2) == 1
assert t.searchInsert([1,3,5,6], 7) == 4
assert t.searchInsert([1,3,5,6], 0) == 0

print "test passed"
