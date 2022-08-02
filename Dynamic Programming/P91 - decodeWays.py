class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0]*(n)
        dp[0] = 1
        
        for i in range(1, n):
            if s[i-1] == "0" and s[i] == "0":
                # if prev char and curr char both are 0 then we 
                # cannot form any combinations
                # say if we had 200, at first we get B
                # when we reach 20, we have T, as soon as we reach 200
                # we will have 2 zeros and we cant form any combination
                dp[i] = 0
                
            elif s[i-1] == "0" and s[i] != "0":
                # if we have say 06, or 08 , we can take atleast the 6
                # say we have 206, at 2 we will have B, 20 T and 206 TF
                # hence we will just take last value 
                dp[i] = dp[i-1]
            elif s[i-1] != "0" and s[i] == "0":
                # in this case we have 10,20,30 etc, we need to check if its
                # less than 26
                # and we will have to take prev prev value
                # if we had 220. at 2 we form B, 22 we for BB, V
                # at 220 we can for only BV, hence i-2
                if s[i-1] == "1" or s[i-1] == "2":
                    dp[i] = dp[i-2] if i >= 2 else 1
                    # because say if we just have 26
                    # when we access i-2 its out of bounds hence we store 1
                else:
                    dp[i] = 0
            elif s[i-1] != "0" and s[i] != "0":
                # so here all combination should be 11-> 26 only
                # so here we can be 1 or 11 with previous values
                if 11 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1] + (dp[i-2] if i >= 2 else 1)
                else:
                    # say number is 75 , we could atleast use 7
                    dp[i] = dp[i-1]
        return dp[n-1]
                    