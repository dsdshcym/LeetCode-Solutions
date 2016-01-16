class Solution(object):
    def insert(self, nums, m, x):
        for i in range(m):
            if x < nums[i]:
                nums.insert(i, x)
                return
        nums.insert(m, x)

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            self.insert(nums1, m, num)
            m += 1
        while len(nums1) > m:
            nums1.pop()

nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
Solution().merge(nums1, 3, nums2, 3)
assert nums1 == [1, 2, 3, 4, 5, 6]

nums1 = [0]
nums2 = [1]
Solution().merge(nums1, 0, nums2, 1)
assert nums1 == [1]

print("tests passed")
