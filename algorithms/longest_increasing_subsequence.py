class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binary_search(x, s):
            N = len(s)
            l, r = 0, N - 1
            while 0 <= l < r < N:
                mid = (l + r) >> 1
                if s[mid] == x:
                    return mid
                if s[mid] < x:
                    l = mid + 1
                if s[mid] > x:
                    r = mid
            return r

        s = []
        for x in nums:
            if not s or x > s[-1]:
                s.append(x)
            else:
                i = binary_search(x, s)
                s[i] = min(s[i], x)
        return len(s)

t = Solution()
assert(t.lengthOfLIS([]) == 0)
assert(t.lengthOfLIS([1]) == 1)
assert(t.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
assert(t.lengthOfLIS([10, 9, 2, 5, 3, 4]) == 3)
assert(t.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6)
assert(t.lengthOfLIS([11, 12, 13, 14, 15, 6, 7, 8, 101, 18]) == 6)
print("tests passed")
