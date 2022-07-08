class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m, n = len(s1), len(s2)
        if(len(s3) != m+n):
            return False
        
        dp = [[False]*(n+1) for i in range(m+1)]
        
        
        # Every cell of Dp will represent that combining s1 s2 , do we have that result in s3 or not
        # for example if s1 = aabcc , s2 = dbbca , s3 = aadbbcbcac
        # if we check cell 4,4 which will form ac, a from s2, c from s1
        # and we will check that last two letters of s3 in our case "ac" match 
        # or not, if they do , as here, we update cell to True else False
        dp[m][n] = True
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if(i < m and s1[i] == s3[i+j] and dp[i+1][j]):
                    dp[i][j] = True
                if(j < n and s2[j] == s3[i+j] and dp[i][j+1]):
                    dp[i][j] = True
        
        return dp[0][0]


        