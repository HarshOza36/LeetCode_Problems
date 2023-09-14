class Solution:
    def canJump(self, nums: List[int]) -> bool:
         # O(n^2) time O(n) space
    #    n = len(nums)
    #    dp = [False] * n
    #    dp[n-1] = True
    #    for i in range(n-2, -1, -1):
    #        for j in range(i+1, min(n, i+nums[i]+1)):
    #            if dp[j]:
    #                dp[i] = True
    #                break
    #    return dp[0]

        n = len(nums)
        max_i = 0
        if(n == 1): 
            return 1
        for i in range(n):
            if(max_i >= i):
                max_i = max(max_i, i + nums[i])
        
        return max_i >= (n-1)