class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        
        r = n - 1
        ans = float(-inf)
        
        while l <= r:
            area = (r-l) * min(height[l], height[r])
            ans = max(ans, area)
            if height[l] <height[r]:
                l += 1
            else:
                r -= 1
        return ans
                