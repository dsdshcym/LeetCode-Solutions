from collections import defaultdict

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = defaultdict(bool)
        for num in nums:
            hash_table[num] = True

        ans = 0
        for num in nums:
            if hash_table[num]:
                hash_table[num] = False
                lcs = 1
                i = num + 1
                while hash_table[i]:
                    hash_table[i] = False
                    i += 1
                    lcs += 1

                i = num - 1
                while hash_table[i]:
                    hash_table[i] = False
                    i -= 1
                    lcs += 1

                if lcs > ans:
                    ans = lcs

        return ans
