class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1, n2 = len(word1), len(word2)
        
        if word1 == word2:
            return 0
        
        
        dp = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]
        
        # Base cases
        dp[-1][-1] = 0
        for j in range(n2 + 1):
            dp[n1][j] = n2 - j
        for i in range(n1 + 1):
            dp[i][n2] = n1 - i
        
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]
        