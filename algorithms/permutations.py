class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        visited = [False, ] * N
        ans = []

        def dfs(remain, permutation):
            if remain == 0:
                ans.append(permutation)
                return
            for i, num in enumerate(nums):
                if not visited[i]:
                    visited[i] = True
                    dfs(remain-1, permutation + [num])
                    visited[i] = False

        dfs(N, [])
        return ans

t = Solution()
print(t.permute([1, 2, 3]))
