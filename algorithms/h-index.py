class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        N = len(citations)
        for i in range(N, 0, -1):
            if citations[N - i] >= i:
                return i
        return 0

t = Solution()
citations = [3, 0, 6, 1, 5, 2]
assert t.hIndex(citations) == 3
citations = [100]
assert t.hIndex(citations) == 1
print("tests passed")
