class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r - 1:
            mid = (l + r) >> 1
            count = 0
            for num in nums:
                if mid < num <= r:
                    count += 1
            if count > r - mid:
                l = mid
            else:
                r = mid
        return r

t = Solution()
assert(t.findDuplicate([7, 9, 7, 4, 2, 8, 7, 7, 1, 5]) == 7)
assert(t.findDuplicate([1, 3, 4, 2, 4]) == 4)
assert(t.findDuplicate([1, 3, 1, 2, 4]) == 1)
assert(t.findDuplicate([1, 3, 3, 2, 4]) == 3)
assert(t.findDuplicate([1, 2, 3, 4, 5, 6, 6, 7, 8]) == 6)
print("tests passed")
