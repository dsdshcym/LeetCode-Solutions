class Solution(object):
    def origin_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0
        max_rob = [nums[0]]
        max_not_rob = [0]
        for i in range(1, N):
            max_rob.append(max_not_rob[i - 1] + nums[i])
            max_not_rob.append(max(max_rob[i - 1], max_not_rob[i - 1]))
        return max(max_rob[N - 1], max_not_rob[N - 1])

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            return max(self.origin_rob(nums[1:]), self.origin_rob(nums[:-1]), nums[0])
        else:
            return 0

t = Solution()
assert(t.rob([]) == 0)
assert(t.rob([0, 0, 0]) == 0)
assert(t.rob([1, 1, 1]) == 1)
assert(t.rob([1, 3, 4, 1]) == 5)
print("tests passed")
