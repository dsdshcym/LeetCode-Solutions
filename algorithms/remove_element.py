class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = 0
        for num in nums:
            if num != val:
                nums[p] = num
                p += 1
        for i in xrange(p, len(nums)):
            nums.pop()
        return len(nums)

t = Solution()
nums = [0, 1, 0, 3, 1]
assert t.removeElement(nums, 0) == 3
assert nums == [1, 3, 1]
nums = [0, 0, 1]
assert t.removeElement(nums, 0) == 1
assert nums == [1]
print "tests passed"
