class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while(n):
            # bitwise and with 1 to check if last digit is one
            # for example 1011 ie 11 & 0001 ie 1 we will get answer 1
            cnt += n & 1
            # right shift by 1
            # 1011 >> 1 = 101
            n >>= 1
        return cnt