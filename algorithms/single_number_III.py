from operator import xor

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_result = reduce(xor, nums)
        mask = xor_result & (-xor_result)
        a = reduce(xor, [num for num in nums if num & mask])
        b = reduce(xor, [num for num in nums if not num & mask])
        return [a, b]
