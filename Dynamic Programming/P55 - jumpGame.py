class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_i = 0
        if(n == 1): 
            return 1
        for i in range(n):
            if(max_i >= i):
                max_i = max(max_i, i + nums[i])
        
        return max_i >= (n-1)