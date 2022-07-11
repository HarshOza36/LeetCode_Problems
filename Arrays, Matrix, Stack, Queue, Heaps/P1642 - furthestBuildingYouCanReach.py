from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights) - 1
        heap = []
        # we will use an approach where we will use always ladders, and as soon as ladders end we use bricks as per the height diff
        # we will use heap to store the height diff
        # every time, we will check if height diff > 0 push to heap
        # if size of queue  will be graeter than total ladders
        # we will then have to use bricks for one move, we pop the min difference from heap, and decrement that from bricks
    
        
        for i in range(n):
            h = heights[i + 1] - heights[i] 
            if(h < 0): continue
                
            if h > 0:
                heappush(heap, h)
            if(len(heap) > ladders):
                bricks -= heappop(heap)
            if(bricks < 0):
                return i
        return n
                