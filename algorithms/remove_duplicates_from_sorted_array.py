class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        count = 0
        for i, num in enumerate(nums[1:], 1):
            if num != nums[count]:
                count += 1
                nums[count] = num
        return count + 1

t = Solution()
assert t.removeDuplicates([1, 1, 2]) == 2
assert t.removeDuplicates([]) == 0
print("tests passed")
