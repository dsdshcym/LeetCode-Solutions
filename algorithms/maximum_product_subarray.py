class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive, negtive, ans = 1, 1, max(nums)
        for num in nums:
            if num > 0:
                positive, negtive = max(positive * num, num), negtive * num
            else:
                positive, negtive = negtive * num, min(positive * num, num)
            ans = max(ans, positive)
        return max(ans, max(nums))

t = Solution()
assert(t.maxProduct([2, 3, -1, 4]) == 6)
assert(t.maxProduct([-2]) == -2)
print("tests passed")
