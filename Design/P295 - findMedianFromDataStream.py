from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        # to find median we need the middle element in sorted list
        # so we will need to get two halfs
        # we will have two heaps
        # the maxHeap will store elements which are low side of the half
        # the minHeap will store elements which are high side of the half
        # so when we look at the root of both
        # we will get the lowest max and highest mid, hence getting
        # middle elements of the sorted list.
        self.maxHeap = [] 
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # we add the stream num to maxHeap
        # but then we may have a high value element which we dont want
        # so we pop it and add to the minHeap
        # next since we are doing this adjustment, we also need to check
        # if we are creating a perfect half
        # so we will check that if minheap size is greater, we will
        # pop from minHeap and add that to maxHeap
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        
    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()