class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, N = 0, len(nums)
        while i < N:
            while 0 < nums[i] <= N and nums[nums[i]-1] != nums[i]:
                if 0 < nums[nums[i]-1] <= N:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                else:
                    nums[nums[i]-1] = nums[i]
            i += 1

        for i, num in enumerate(nums, 1):
            if num != i:
                return i
        return N + 1

t = Solution()
assert(t.firstMissingPositive([2, 1]) == 3)
assert(t.firstMissingPositive([1, 2]) == 3)
assert(t.firstMissingPositive([1]) == 2)
assert(t.firstMissingPositive([6]) == 1)
print("tests passed")
