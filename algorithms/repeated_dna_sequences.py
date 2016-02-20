class Solution(object):
    DNA_BIT = {
        "A": "0",
        "C": "1",
        "G": "2",
        "T": "3",
    }
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_in_bits = ''.join([self.DNA_BIT[c] for c in s])
        hash_values = {}
        ans = []
        for i in range(len(s)-9):
            cur = s[i:i+10]
            if cur in hash_values and cur not in ans:
                ans.append(cur)
            else:
                hash_values[cur] = int(s_in_bits[i:i+10], 4)
        return ans

t = Solution()
print(t.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(t.findRepeatedDnaSequences("AAAAAAAAAAA"))
