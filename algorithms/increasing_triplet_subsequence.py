class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        min_before, max_after = list(nums), list(nums)
        for i in range(1, N):
            min_before[i] = min(min_before[i-1], min_before[i])
            max_after[N-1-i] = max(max_after[N-i], max_after[N-1-i])
        for i in range(1, N-1):
            if min_before[i] < nums[i] < max_after[i]:
                return True
        return False

t = Solution()
assert(t.increasingTriplet([1, 2, 3, 4, 5]))
assert(not t.increasingTriplet([5, 4, 3, 2, 1]))
print("tests passed")
