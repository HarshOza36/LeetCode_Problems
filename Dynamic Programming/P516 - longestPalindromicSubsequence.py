class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0]*n for _ in range(n)]

        for g in range(n):
            for j in range(g, n):
                i = j - g
                if g == 0:
                    # all same
                    dp[i][j] = 1
                elif g == 1:
                    # second diagonal 2 elements
                    dp[i][j] = 2 if s[i] == s[j] else 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]