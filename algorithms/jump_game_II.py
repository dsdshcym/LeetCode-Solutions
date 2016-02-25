class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        near, far, step = 0, 1, 0
        while far < len(nums):
            new_far = max(start + step + 1
                          for start, step in zip(range(near, far),
                                                 nums[near:far]))
            near, far, step = far, new_far, step + 1
        return step

t = Solution()
assert(t.jump([0]) == 0)
assert(t.jump([2,3,1,1,4]) == 2)
print("tests passed")
