class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
##        Tabulation
##        dp = [0, 1]
##        for i in range(2, n + 1):
##            dp.append(dp[i-1] + dp[i-2])
##        return dp[n]

##        Memoized
        d = {}
        
        def fibo_r(n):
            if(n in d): return d[n]
            if(n < 2): 
                res = n
            else: 
                res = fibo_r(n-1) + fibo_r(n-2)
            
            d[n] = res
            return res
        
        return fibo_r(n)
