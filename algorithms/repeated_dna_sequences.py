class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        record, ans = set(), set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in record:
                ans.add(sub)
            else:
                record.add(sub)
        return list(ans)

t = Solution()
print(t.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(t.findRepeatedDnaSequences("AAAAAAAAAAA"))
