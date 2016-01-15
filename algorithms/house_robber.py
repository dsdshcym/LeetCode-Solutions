class Solution(object):
    def rob(self, nums):
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

t = Solution()
assert t.rob([5, 1, 1, 5]) == 10
assert t.rob([5, 1, 5, 1]) == 10
print("tests passed")
