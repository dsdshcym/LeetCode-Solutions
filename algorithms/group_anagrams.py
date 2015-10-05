class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs = sorted(strs)
        original_strs = list(strs)
        N = len(strs)
        for i in xrange(N):
            strs[i] = ''.join(sorted(list(strs[i])))
        visited = [False for _ in xrange(N)]
        ans = []
        for i in xrange(N):
            if not visited[i]:
                temp_list = []
                for j in xrange(i, N):
                    if strs[j] == strs[i]:
                        temp_list.append(original_strs[j])
                        visited[j] = True
                ans.append(temp_list)
        return ans

t = Solution()
case = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = [
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
print t.groupAnagrams(case)
assert(t.groupAnagrams(case) == ans)
