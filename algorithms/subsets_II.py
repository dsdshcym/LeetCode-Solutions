class Solution(object):
    def dfs(self, nums, index, path, ans):
        ans.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], ans)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans

t = Solution()

# print t.subsetsWithDup([1, 2, 3])
print t.subsetsWithDup([1, 1])
