class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        ans = start
        for i in range(1,n):
            ans = ans ^ (start + 2*(i))
        return ans