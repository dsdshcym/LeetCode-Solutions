class Solution(object):
    def dfs(self, nums, sub):
        if nums == []:
            self.ans.append(sub)
            return
        self.dfs(nums[1:], sub + [nums[0]])
        self.dfs(nums[1:], sub)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(set(nums))
        self.ans = []
        self.dfs(nums, [])
        return self.ans

t = Solution()

print t.subsets([1, 2, 3])
