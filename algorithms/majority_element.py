class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        for x in nums:
            if count == 0:
                ans = x
            if ans == x:
                count += 1
            else:
                count -= 1
        return ans

t = Solution()

assert t.majorityElement([1, 1, 2]) == 1
assert t.majorityElement([1]) == 1

print("tests passed")
