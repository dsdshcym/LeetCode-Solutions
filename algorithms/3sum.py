class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = set()
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                z = -(x + y)
                if z in nums[i+j+2:]:
                    ans.add((x, y, z))
        return list(ans)

nums = [-1, 0, 1, 2, -1, -4]
assert Solution().threeSum(nums) == [(-1, -1, 2), (-1, 0, 1)]
nums = []
assert Solution().threeSum(nums) == []
nums = [0, 0, 0, 0]
assert Solution().threeSum(nums) == [(0, 0, 0)]

print("tests passed")
