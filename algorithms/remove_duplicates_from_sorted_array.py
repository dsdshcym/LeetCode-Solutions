class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

t = Solution()
assert t.removeDuplicates([1, 1, 2]) == 2
assert t.removeDuplicates([]) == 0
print("tests passed")
