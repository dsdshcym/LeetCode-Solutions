class Solution(object):
    def __init__(self):
        self.ans = []

    def addRange(self, begin, end):
        begin = str(begin)
        end = str(end)
        if begin != end:
            self.ans.append(begin + '->' + end)
        else:
            self.ans.append(begin)

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        begin = pre = nums[0]
        for x in nums[1:-1]:
            if x != pre + 1:
                end = pre
                self.addRange(begin, end)
                begin = x
            pre = x
        self.addRange(begin, nums[-1])
        return self.ans

assert Solution().summaryRanges([0, 1, 2, 4, 7, 8]) == ['0->2', '4', '7->8']
print("tests passed")
