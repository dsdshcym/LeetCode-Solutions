class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        N = len(nums)
        for i in range(N):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

t = Solution()
assert(t.canJump([2, 3, 1, 1, 4]))
assert(not t.canJump([3, 2, 1, 0, 4]))
print("tests passed")
