# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals = sorted(intervals, cmp = lambda x, y: cmp(x.start, y.start))
        ans = []
        new_interval = intervals[0]
        for interval in intervals[1:]:
            if new_interval.end >= interval.start:
                if interval.end > new_interval.end:
                    new_interval.end = interval.end
            else:
                ans.append(new_interval)
                new_interval = interval
        ans.append(new_interval)
        return ans

t = Solution()

assert(t.merge([]) == [])

a = Interval(1, 3)
b = Interval(2, 6)
c = Interval(8, 10)
d = Interval(15, 18)
case = [a, b, c, d]

ans = t.merge(case)
for inte in ans:
    print inte.start, inte.end
