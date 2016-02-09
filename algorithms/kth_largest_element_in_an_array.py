class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def pivot(nums, l, r):
            p = l
            closed = p
            for i in xrange(l, r):
                if nums[i] < nums[p]:
                    closed += 1
                    nums[i], nums[closed] = nums[closed], nums[i]
            nums[closed], nums[p] = nums[p], nums[closed]
            return closed

        def find(nums, l, r, k):
            if l >= r:
                return

            p = pivot(nums, l, r)
            if k == p:
                return nums[p]
            if k < p:
                return find(nums, l, p, k)
            return find(nums, p+1, r, k)

        return find(nums, 0, len(nums), len(nums)-k)

t = Solution()
# assert(t.findKthLargest([5, 2, 4, 1, 3, 6, 0], 4) == 3)
# assert(t.findKthLargest([3, 1, 2, 4], 2) == 3)
assert(t.findKthLargest([1, 2, 3], 1) == 3)
assert(t.findKthLargest([1, 2, 3], 2) == 2)
assert(t.findKthLargest([3, 2, 3], 2) == 3)
assert(t.findKthLargest([1], 1) == 1)
print("tests passed")
