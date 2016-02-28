class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
            index -= 1

        nums1[:n+1] = nums2[:n+1]

nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]
Solution().merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 3, 4, 5, 6]

nums1 = [0]
nums2 = [1]
Solution().merge(nums1, 0, nums2, 1)
assert nums1 == [1]

print("tests passed")
