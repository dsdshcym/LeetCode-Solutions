from sys import maxint

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            return (self.find_kth(nums1, nums2, l // 2) + \
                self.find_kth(nums1, nums2, l // 2 + 1)) / 2.0
        else:
            return self.find_kth(nums1, nums2, l // 2 + 1)

    def find_kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        key1 = nums1[k // 2 - 1] if k // 2 <= len(nums1) else maxint
        key2 = nums2[k // 2 - 1] if k // 2 <= len(nums2) else maxint
        if key1 < key2:
            return self.find_kth(nums1[k // 2:], nums2, k - k // 2)
        else:
            return self.find_kth(nums1, nums2[k // 2:], k - k // 2)

t = Solution()
assert(t.findMedianSortedArrays([1, 3, 5], []) == 3)
assert(t.findMedianSortedArrays([1, 3, 5], [2, 4]) == 3)
assert(t.findMedianSortedArrays([1, 3, 5], [2, 4, 6]) == 3.5)
print("tests passed")
