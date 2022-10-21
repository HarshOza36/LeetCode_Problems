class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x2,y2):
            # x1,y1 are 0,0 origin
            return ((x2-0)**2 + (y2-0)**2)**0.5
        
        heap = []
        
        # O(nlogn)
        for idx, (x2,y2) in enumerate(points):
            heappush(heap,(distance(x2,y2), [x2,y2]))
        ans = []
        # O(klogn)
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans
        