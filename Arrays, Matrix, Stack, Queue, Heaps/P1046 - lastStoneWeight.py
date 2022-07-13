class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
            
        while len(heap) > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            print(x,y, heap)
            if(x != y):
                heapq.heappush(heap, (y-x))
        return -heap[0] if heap else 0