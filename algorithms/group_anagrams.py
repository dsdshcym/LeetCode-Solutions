class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        temp = []
        strs = sorted(strs, cmp=lambda x, y: cmp(sorted(x), sorted(y)))
        for i in xrange(len(strs) - 1):
            temp.append(strs[i])
            if sorted(strs[i]) != sorted(strs[i + 1]):
                ans.append(sorted(temp))
                temp = []
        temp.append(strs[-1])
        ans.append(sorted(temp))
        return ans

t = Solution()
case = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = [
    ["ate", "eat","tea"],
    ["nat","tan"],
    ["bat"]
]
print t.groupAnagrams(case)
print t.groupAnagrams([""])
assert(t.groupAnagrams([""]) == [[""]])
