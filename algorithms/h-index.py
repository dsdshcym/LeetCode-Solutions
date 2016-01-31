class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0,] * (N + 1)
        for c in citations:
            if c > N:
                count[N] += 1
            else:
                count[c] += 1
        c = 0
        for i in range(N, -1, -1):
            c += count[i]
            if c >= i:
                return i

t = Solution()
citations = [3, 0, 6, 1, 5, 2]
assert t.hIndex(citations) == 3
citations = [100]
assert t.hIndex(citations) == 1
citations = [0]
assert t.hIndex(citations) == 0
print("tests passed")
