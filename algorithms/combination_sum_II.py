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

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        N = len(candidates)
        ans = []
        candidates.sort()
        for i in range(N):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] == target:
                ans.append([candidates[i]])
            elif candidates[i] > target:
                break
            else:
                ans.extend([[candidates[i]] + l
                            for l in self.combinationSum2(candidates[i+1:], target-candidates[i])
                            if l])
        return ans

t = Solution()
print(t.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(t.combinationSum2([1], 1))
