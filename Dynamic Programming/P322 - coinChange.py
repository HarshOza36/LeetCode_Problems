class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
#         # O(c * amount) time and space
#         if amount == 0:
#             return 0
#         c = len(coins)
#         dp = [[float('inf')] * (amount + 1) for _ in range(c + 1)]
        
#         for i in range(c+1):
#             dp[i][0] = 1
        
#         for i in range(1, c+1):
#             for j in range(1, amount + 1):
#                 if j - coins[i-1] == 0:
#                     dp[i][j] = 1
#                 elif j - coins[i-1] < 0:
#                     dp[i][j] = dp[i-1][j]
#                 else:
#                     dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])

#         return -1 if dp[c][amount] == float('inf') else dp[c][amount]
        
        # optimizing space now O(amount) space, and O(c*amount) time
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                if(i - coin)>= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[-1] == float("inf") else dp[-1]
