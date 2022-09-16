class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0] * len(prices) for i in range(k+1)]
        
        for t in range(1,k+1):
            currMax = float(-inf)
            for d in range(1,len(prices)):
                currMax = max(currMax, dp[t-1][d-1] - prices[d-1])
                dp[t][d] = max(currMax + prices[d], dp[t][d-1])
        return dp[k][len(prices)-1]