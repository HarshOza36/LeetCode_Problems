class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # below solution is pretty fast
        # return x**n
        
        # Below gives Max recursion depth so added recursion limit, still TLE
        # import sys
        # sys.setrecursionlimit(10**6)
        # temp = 0
        # if(n == 0):
        #     return 1
        # temp = self.myPow(x, int(n / 2))
        # if (n % 2 == 0):
        #     return temp * temp
        # else:
        #     return x * temp * temp
        
        # Below recursion solution is not the fastest but it passes all test cases.
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1 / x
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        return (self.myPow(x, n // 2) ** 2) * x
