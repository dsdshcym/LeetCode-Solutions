class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        flag = False
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                if flag:
                    nums.pop(i)
                else:
                    flag = True
                    i += 1
            else:
                flag = False
                i += 1
        return len(nums)

t = Solution()
assert t.removeDuplicates([1, 1, 2]) == 3
assert t.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
assert t.removeDuplicates([]) == 0
print("tests passed")
