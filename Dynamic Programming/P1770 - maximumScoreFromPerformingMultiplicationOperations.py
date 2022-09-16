class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
#         n,m = len(nums), len(multipliers)
#         dp = [[0]*(m+1) for i in range(m+1)]
        
#         for i in range(m-1,-1,-1):
#             for l in range(i, -1,-1):
#                 # we take left, and add next iteration left
#                 path1 = multipliers[i] * nums[l] + dp[i+1][l+1]
                
#                 # we take right here we see right is (n-1) - (i-l)
#                 # it is because say i is 4, and l = 2, this means
#                 # that we traversed 4 elements in multipliers, and from 
#                 # left we just took 2, hence from right as well we took 2
#                 # that is i-l ie 4-2 = 2
#                 # we do n-1 - this value, so that we get the index from end
#                 # of array to get right index
                
#                 # so we take the right, and next iterations of right
#                 path2 = multipliers[i] * nums[(n-1)-(i-l)] + dp[i+1][l]
#                 dp[i][l] = max(path1, path2)
#         return dp[0][0]
    
        # optimizing above approach
        n,m = len(nums), len(multipliers)
        dp = [0] * (m + 1)
        for i in range(m-1, -1, -1):
            temp = [0] * (i + 1)
            for l in range(i, -1, -1):
                temp[l] = max(dp[l + 1] + multipliers[i] * nums[l], 
                            dp[l] + multipliers[i] * nums[~(i-l)])
            dp = temp
        return dp[0]