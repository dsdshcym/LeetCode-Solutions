class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = [max(nums[:k])]
        for i in range(k, len(nums)):
            if nums[i] >= ans[i-k]:
                new_max = nums[i]
            else:
                if ans[i-k] == nums[i-k]:
                    new_max = max(nums[i-k+1:i+1])
                else:
                    new_max = ans[i-k]
            ans.append(new_max)
        return ans
