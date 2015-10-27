from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = defaultdict(list)
        ans = list()
        for s in strs:
            h[''.join(sorted(s))].append(s)
        for key in h.keys():
            ans.append(sorted(h[key]))
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
