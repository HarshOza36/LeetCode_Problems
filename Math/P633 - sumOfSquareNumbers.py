class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        from math import sqrt
        l,r = 0, int(sqrt(c))
        while(l <= r):
            curr = l*l + r*r
            if(curr == c): 
                return True
            if(curr < c):
                l += 1
            else:
                r -= 1
        return False