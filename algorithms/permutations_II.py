class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return reduce(lambda perms, num:
                      [p[:i] + [num] + p[i:]
                       for p in perms
                       for i in range((p + [num]).index(num)+1)],
                      nums, [[]])

        perms = [[]]
        for num in nums:
            perms = [p[:i] + [num] + p[i:]
                     for p in perms
                     for i in range((p + [num]).index(num)+1)]
        return perms

t = Solution()
print(t.permuteUnique([1, 1, 2]))
