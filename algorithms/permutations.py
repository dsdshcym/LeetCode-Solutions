class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return reduce(lambda perms, num:
                      [p[:i] + [num] + p[i:]
                       for p in perms
                       for i in range(len(p)+1)],
                      nums, [[]])

        perms = [[]]
        for num in nums:
            perms = [p[:i] + [num] + p[i:]
                     for p in perms
                     for i in range(len(p)+1)]
        return perms

t = Solution()
print(t.permute([1, 2, 3]))
