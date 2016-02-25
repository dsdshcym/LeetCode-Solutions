class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        max_index = [0 for i in range(N+1)]
        for i, step in enumerate(nums):
            for j in range(N):
                if i <= max_index[j]:
                    break
            # if i > max_index[j]:
            #     raise Exception
            new_max_index = i + step
            max_index[j + 1] = max(max_index[j + 1],new_max_index)

        for i, index in enumerate(max_index):
            if index >= N - 1:
                return i

t = Solution()
assert(t.jump([0]) == 0)
assert(t.jump([2,3,1,1,4]) == 2)
print("tests passed")
