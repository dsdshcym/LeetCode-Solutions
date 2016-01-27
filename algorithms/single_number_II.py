class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_1 = 0
        count_2 = 0
        for num in nums:
            count_1 = (~count_2) & (count_1 ^ num)

            # The count_1 here is the new count_1
            count_2 = (~count_1) & (count_2 ^ num)

        return count_1

t = Solution()
assert(t.singleNumber([2, 2, 3, 2]) == 3)
print("tests passed")
