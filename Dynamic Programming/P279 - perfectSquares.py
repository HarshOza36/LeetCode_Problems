class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        for k in range(1, n+1):
            dp[k] = min(1 + dp[k - i*i] for i in range(int(k**0.5), 0, -1))
        return dp[n]