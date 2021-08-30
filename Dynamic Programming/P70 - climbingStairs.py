class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        def cs_rec(n):
            if(n in d): return d[n]
            if(n <= 2):
                return n
            else:
                res = cs_rec(n-1)+cs_rec(n-2)
            d[n] = res
            return res
        return cs_rec(n)
        