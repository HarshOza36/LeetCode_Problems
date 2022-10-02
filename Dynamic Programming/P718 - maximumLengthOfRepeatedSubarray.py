class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        # this is basically, longest common substring
        # if we have abcba and cbafe, that is in form 1,2,3,2,1 and 3,2,1,5,4
        # we return 3 because we have cba or 321
        
        m, n = len(nums1), len(nums2)
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        currMax = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    currMax = max(currMax, dp[i+1][j+1])
        return currMax