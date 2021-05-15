class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = x
        x = str(abs(x))
        out = int(x[::-1])
        if(out > 2**31 -1 or out < -2**31):
            return 0
        elif(num < 0):
            return -1*out
        else:
            return out