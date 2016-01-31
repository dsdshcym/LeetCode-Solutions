class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        if n == k:
            return [range(1, n+1)]
        if k == 0:
            return [[]]
        return self.combine(n - 1, k) + [l + [n]
                                         for l in self.combine(n - 1, k - 1)]
