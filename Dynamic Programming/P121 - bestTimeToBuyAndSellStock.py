class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        # Setting first value in table with min price and max profit
        dp[0] = [prices[0], 0] 
        
        for i in range(1,n):
            dp[i][0] = min(dp[i-1][0], prices[i]) # min(prev_minPrice, cur_minPrice)
            dp[i][1] = max(dp[i-1][1], prices[i] - dp[i-1][0]) # max(prev_maxProfit, curr_profit)
        # Returning the maximum profit that will be available        
        return dp[n-1][1]