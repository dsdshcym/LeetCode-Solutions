class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ans, max_covered = 0, 0
        nums.append(n+1)
        for num in nums:
            num = min(num, n+1)
            while max_covered < num - 1:
                max_covered += max_covered + 1
                ans += 1
            max_covered += num
        return ans

t = Solution()
assert(t.minPatches([1, 5, 10], 20) == 2)
print("tests passed")
