class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i, x in enumerate(nums):
            if target - x in hash_dict:
                return [hash_dict[target - x], i]
            else:
                hash_dict[x] = i

t = Solution()
assert(t.twoSum([2, 7, 11, 15], 9) == [0, 1])
assert(t.twoSum([3, 2, 4], 6) == [1, 2])
print("tests passed")
