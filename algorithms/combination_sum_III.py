class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        self.combinationSum3_helper(k, n, [], 0, 0, ans)
        return ans

    def combinationSum3_helper(self, k, n, combination, i, s, ans):
        if len(combination) == k and s == n:
            ans.append(combination)
            return
        if s > n or i == 9:
            return
        for j in range(i + 1, 10):
            self.combinationSum3_helper(k, n, combination + [j], j, s + j, ans)
