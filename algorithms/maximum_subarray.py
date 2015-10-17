class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        m = max(nums)
        for num in nums:
            if s + num > 0:
                s += num
                if s > m:
                    m = s
            else:
                s = 0
        return m

t = Solution()

assert t.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert t.maxSubArray([1]) == 1
assert t.maxSubArray([-2, -1]) == -1

print "tests passed"
