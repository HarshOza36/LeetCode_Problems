class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # we will get xor which gives 1 when we have different bits
        xor = x ^ y
        # count all 1s
        cnt = 0
        while(xor):
            # bitwise and with 1 to check if last digit is one
            # for example 1011 ie 11 & 0001 ie 1 we will get answer 1
            cnt += xor & 1
            # right shift by 1
            # 1011 >> 1 = 101
            xor >>= 1
        return cnt