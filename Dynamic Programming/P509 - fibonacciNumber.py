class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
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