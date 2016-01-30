class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        lis = []
        for i, num in enumerate(nums):
            temp = max([0] + [lis[j] for j, x in enumerate(nums[:i]) if x < num]) + 1
            ans = max(ans, temp)
            lis.append(temp)
        return ans

t = Solution()
assert(t.lengthOfLIS([]) == 0)
assert(t.lengthOfLIS([1]) == 1)
assert(t.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
print("tests passed")
