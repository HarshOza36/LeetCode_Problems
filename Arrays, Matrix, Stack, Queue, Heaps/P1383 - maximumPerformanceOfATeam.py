class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engr = []
        
        # Sorting the speed as per the efficiency 
        for eff, spd in zip(efficiency, speed):
            engr.append([eff, spd])
        engr.sort(reverse = True)
        
        ans, speed = 0, 0
        minHeap = []
        
        # Now we will add all speed values in the minHeap and keep the currSpeed
        # a soon as we reach K elements, we remove the first seen min value 
        # from the heap and also deduct it from current Speed
        # so we will keep the higher speeds in the minHeap
        # and when we loop we are always considering the minimum effiency
        # since we are going descending to ascending
        
        for eff, spd in engr:
            
            if len(minHeap) == k:
                speed -= heappop(minHeap)
            
            speed += spd
            heappush(minHeap, spd)

            ans = max(ans, eff * speed)
        return ans % (10**9 + 7)