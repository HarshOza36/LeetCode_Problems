class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[(0,False)]*n for _ in range(n)]
        
        for g in range(n):
            for j in range(g, n):
                i = j-g
                if(g == 0):
                    # its the diag
                    dp[i][j] = (1,True)
                elif(g == 1):
                    # second diag we could just check both places
                    if(s[i] == s[j]):
                        dp[i][j] = (dp[i+1][j][0] + dp[i][j-1][0] + 1, True)
                    else:
                        dp[i][j] = (dp[i+1][j][0] + dp[i][j-1][0], False)
                else:
                    if(s[i] == s[j] and dp[i+1][j-1][1]):
                        # if edges are same and diag is palindrome
                        dp[i][j] = (dp[i+1][j][0] + dp[i][j-1][0] + 1 - dp[i+1][j-1][0], True)
                    else:
                        dp[i][j] = (dp[i+1][j][0] + dp[i][j-1][0] - dp[i+1][j-1][0], False)
        return dp[0][n-1][0]