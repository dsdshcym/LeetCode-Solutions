class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n < 3:
            raise
        nums.sort()
        result = sum(nums[:3])
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                result = min(s, result, key=lambda x: abs(x - target))
                if s == target:
                    return s
                k -= s > target
                j += s < target
        return result

t = Solution()
assert(t.threeSumClosest([-1, 2, 1, -4], 1) == 2)
assert(t.threeSumClosest([0, 1, 2], 3) == 3)
assert(t.threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82) == 82)
print('tests passed')
