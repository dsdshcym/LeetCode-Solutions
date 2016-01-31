class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        N = len(citations)
        l, r = 0, N
        while l < r - 1:
            mid = (l + r) >> 1
            if citations[N - mid] >= mid:
                l = mid
            else:
                r = mid
        if citations[N - r] >= r:
            return r
        else:
            return l

t = Solution()
assert(t.hIndex([0, 1, 3, 5, 6]) == 3)
assert(t.hIndex([1]) == 1)
print("tests passed")
