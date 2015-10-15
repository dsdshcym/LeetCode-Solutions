class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in xrange(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

t = Solution()

assert not t.containsDuplicate([])

print "tests passed"
