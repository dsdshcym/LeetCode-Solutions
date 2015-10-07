class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        output = [1 for _ in xrange(N)]
        product = 1
        for i in xrange(N - 1):
            product *= nums[i]
            output[i + 1] *= product
        product = 1
        for i in xrange(N - 1, 0, -1):
            product *= nums[i]
            output[i - 1] *= product
        return output

t = Solution()

assert(t.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])

print "tests passed"
