import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small_heap, self.large_heap = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.small_heap:
            heapq.heappush(self.small_heap, -num)
            return

        if num <= -self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)

        if len(self.small_heap) - len(self.large_heap) == 2:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        if len(self.small_heap) - len(self.large_heap) == -2:
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small_heap) == len(self.large_heap):
            return (self.large_heap[0] - self.small_heap[0]) / 2.0
        if len(self.small_heap) > len(self.large_heap):
            return -float(self.small_heap[0])
        if len(self.large_heap) > len(self.small_heap):
            return float(self.large_heap[0])

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(1)
assert(mf.findMedian() == 1)
mf.addNum(2)
assert(mf.findMedian() == 1.5)
mf.addNum(3)
assert(mf.findMedian() == 2)
print("tests passed")
