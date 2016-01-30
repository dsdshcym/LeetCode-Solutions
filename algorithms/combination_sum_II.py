class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        N = len(candidates)
        ans = []
        candidates.sort()

        def dfs(i, s, attempt):
            if s == target:
                ans.append(attempt)
                return
            if i >= N or s > target:
                return
            for j in range(i, N):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                dfs(j+1, s+candidates[j], attempt+[candidates[j]])

        dfs(0, 0, [])
        return ans

t = Solution()
print(t.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(t.combinationSum2([1], 1))
