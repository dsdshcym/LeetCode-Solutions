class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N, s = len(nums), sum(nums)
        s_origin = sum(range(N + 1))
        ans = s_origin - s
        if ans == 0 and nums[0] == 0:
            return N
        return ans

t = Solution()
print(t.missingNumber([0, 1, 3]))
assert(t.missingNumber([0, 1, 3]) == 2)
print("tests passed")
