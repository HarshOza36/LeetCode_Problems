class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s_nums = sum(nums)
        
        if s_nums & 1:
            return False
        
        target = s_nums // 2
        
#         dp = [[False] * (target + 1) for _ in range(n+1)]
        
#         dp[0][0] = True
#         for i in range(1, n+1):
#             dp[i][0] = True
        
#         for j in range(1, target + 1):
#             dp[0][j] = False
            
            
#         for i in range(1, n+1):
#             for j in range(1, target + 1):
#                 if j < nums[i-1]:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
#         return dp[-1][-1]

        # Improving space
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, -1, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[-1]