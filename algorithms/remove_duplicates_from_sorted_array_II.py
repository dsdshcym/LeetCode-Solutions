class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        count = 1
        for i, num in enumerate(nums[2:], 2):
            if num != nums[count - 1]:
                count += 1
                nums[count] = num
        return count + 1

t = Solution()
assert t.removeDuplicates([1, 1, 2]) == 3
assert t.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
assert t.removeDuplicates([]) == 0
print("tests passed")
