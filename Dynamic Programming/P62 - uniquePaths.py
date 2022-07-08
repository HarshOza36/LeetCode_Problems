class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if(i == m-1 or j == n-1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]