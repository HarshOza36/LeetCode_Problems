class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        
        while n > 1:
            mod = n % 2
            if mod != 0:
                return False
            n /= 2
        
        return True