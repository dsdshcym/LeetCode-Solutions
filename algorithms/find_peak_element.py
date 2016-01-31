from sys import maxint

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        nums.append(-maxint-1)
        while l < r - 1:
            mid = (l + r) >> 1
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return max([l, r], key=lambda x: nums[x])

t = Solution()
assert(t.findPeakElement([1, 2, 3, 1]) == 2)
assert(t.findPeakElement([2, 1, 2]) == 0 or t.findPeakElement([2, 1, 2]) == 2)
print("tests passed")
