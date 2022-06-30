class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # My approach is a sliding window kind 
        # First will sum up and combine all the ones in between zeros
        # We will also store the current max subarray if ones
        # After that will use two pointer approach where,
        # If we find a zero, we will use left sum of ones and add it to 
        # right sum of ones. We will sum them up and then match it with
        # the max subarray we had found and continue till end.
        
#         if(len(nums) <= 1):
#             return 0
#         combine = []
#         cnt = 0
#         maxcnt = float('-inf')
#         for n in nums:
#             if n != 0:
#                 cnt += 1
#             else:
#                 if cnt:
#                     maxcnt = max(maxcnt, cnt)
#                     combine.append(cnt)
#                 combine.append(n)
#                 cnt = 0
#         if nums[-1] != 0: combine.append(cnt)
#         if cnt:
#             maxcnt = max(maxcnt, cnt)
        
#         if(len(combine) == 1):
#             return combine[0] - 1
        
#         ans = maxcnt
#         l,r = 0,1
#         n = len(combine)
#         while(r < n):
#             if(combine[l] == 0):
#                 l += 1
#             if(r+1 < n and combine[r] == 0):
#                 if combine[r+1] > 0:
#                     ans = max(ans, combine[l] + combine[r+1])
#                 l = r + 1
#                 r = l + 1
#             else:
#                 r += 1
#         return 0 if ans == float('-inf') else ans
         
        # Dynamic Programming approach
        # Let dp[i][0] be the length of longest subarray of ones, such that
        # it ends at point i. Let dp[i][1] be the length longest subarray, 
        # which has one zero and ends at point i. Now

        # dp[0][0] = 1 if nums[0] = 1 and 0 otherwise
        # If nums[i] = 1, then to update dp[i][0] we just need to look into   
        # dp[i-1][0] and add one, the same for dp[i][1].
        # If nums[i] = 0, than dp[i][0] = 0, we need to interrupt our 
        # sequence without zeroes. dp[i][1] = dp[i-1][0], because we added 0 
        # and number of 1 is still i-1.
        n = len(nums)
        if sum(nums) == n: 
            return n - 1 # that is all ones.
        
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = nums[0]
        
        for i in range(1, n):
            if nums[i] == 1:
                dp[i][0], dp[i][1] = dp[i-1][0] + 1, dp[i-1][1] + 1
            else:
                dp[i][0], dp[i][1] = 0, dp[i-1][0]
        
        return max([i for j in dp for i in j])  