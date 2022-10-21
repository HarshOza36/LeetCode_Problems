class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n) time and space
#         if not height: return 0
#         maxLheight, maxRheight = [0], [0]*len(height)
        
#         for i in range(1, len(height)):
#             maxLheight.append(max(maxLheight[i-1], height[i-1]))
#             maxRheight[-i-1] = max(maxRheight[-i], height[-i])
        
#         trappedWater = 0
#         for i in range(len(height)):
            
#             # trapped water will be min of left bar and right bar minus 
#             # height of that actual bar
#             # if we get negative we will add 0
#             trappedWater += max(0, min(maxLheight[i], maxRheight[i]) - height[i])
#         return trappedWater
        
        # Optimizing space, O(n) time, O(1) space using two pointers
        if not height: return 0
        n = len(height)
        l = 0
        r = n-1
        maxLeft = height[l]
        maxRight = height[r]
        trappedWater = 0
        # we know that, start left and right bars cannot store water
        # now we will move only that pointer, which has smaller height
        # after that, once we move it, we will find if the height changes
        # for that pointer, and then calculate, that pointer value - height at
        # that pointer
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                trappedWater += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                trappedWater += maxRight - height[r]
        return trappedWater
        
        