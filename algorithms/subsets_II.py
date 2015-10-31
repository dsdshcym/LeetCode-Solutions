class Solution(object):
    def dfs(self, nums, sub):
        if nums == []:
            if sub not in self.ans:
                self.ans.append(sub)
            return
        self.dfs(nums[1:], sub + [nums[0]])
        self.dfs(nums[1:], sub)

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.ans = []
        self.dfs(nums, [])
        return self.ans

t = Solution()

# print t.subsetsWithDup([1, 2, 3])
print t.subsetsWithDup([1, 1])
