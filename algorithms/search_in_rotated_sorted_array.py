class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        l, r = 0, N - 1
        while -1 < l <= r < N:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            if target == nums[l] or \
               target < nums[mid] < nums[l] or \
               nums[l] < target < nums[mid] or \
               nums[mid] < nums[l] < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

t = Solution()
assert(t.search([8, 9, 2, 3, 4], 9) == 1)
assert(t.search([5, 1, 3], 5) == 0)
assert(t.search([5, 1, 2, 3, 4], 1) == 1)
assert(t.search([4, 5, 6, 7, 0, 1, 2], 0) == 4)
assert(t.search([4, 5, 6, 7, 0, 1, 2], 5) == 1)
assert(t.search([1], 1) == 0)
assert(t.search([], 0) == -1)
assert(t.search([1, 3], 0) == -1)
assert(t.search([3, 1], 1) == 1)
print("tests passed")
