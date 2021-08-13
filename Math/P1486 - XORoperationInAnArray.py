class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        out = start
        for i in range(1,n):
            out = out ^ (start+2*i)
        return out