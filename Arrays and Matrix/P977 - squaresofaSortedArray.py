class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        out = [None] * (r+1)
        for i in range(n):
            if(nums[l]**2 > nums[r]**2):
                out[n-i-1] = nums[l]**2
                l += 1
            else:
                out[n-i-1] = nums[r]**2
                r -= 1
            
        return out
            