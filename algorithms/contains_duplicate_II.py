class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        enumerated_nums = sorted(enumerate(nums), cmp = lambda x, y: cmp(x[1], y[1]))
        N = len(nums)
        for i in xrange(N - 1):
            if enumerated_nums[i][1] == enumerated_nums[i + 1][1] and \
               abs(enumerated_nums[i][0] - enumerated_nums[i + 1][0]) <= k:
                return True
        return False

t = Solution()

assert t.containsNearbyDuplicate([99, 99], 2)

print "tests passed"
