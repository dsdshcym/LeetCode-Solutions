#+TAG: NEEDS_IMPROVE

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        ans = N + 1
        head = 0
        tail = -1
        sum_nums = 0
        while (tail < N - 1):
            tail += 1
            sum_nums += nums[tail]
            while (sum_nums - nums[head] >= s):
                sum_nums -= nums[head]
                head += 1
            if (sum_nums >= s) and (tail - head + 1< ans):
                ans = tail - head + 1
        return ans if ans < N + 1 else 0


        # sum_nums = [sum(nums[:i]) for i in xrange(0, N + 1)]
        # if sum_nums[N] < s:
        #     return 0
        # return min((y - x
        #             for x in xrange(N)
        #             for y in xrange(x, N + 1)
        #             if (sum_nums[y] - sum_nums[x] >= s)))

t = Solution()

print t.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
assert(t.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
