class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [0 for _ in range(n+1)]
        dp[n-1] = cost[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        return min(dp[0], dp[1])
            