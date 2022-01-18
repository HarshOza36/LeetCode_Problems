class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Approach : We find 2 numbers with all bits diff in all positions, then use XOR to get 
        # the answer. In order to find such condition, we use XOR to find different bits and then 
        # use Bitwise And (&) left shifted (<<) by 1 to keep all bits updated with carrys if 
        # there are same bits 1 in same postition.
        
        # For Example : 
        # a = 1100, b = 0000
        # a & b = 0000 hence return a ^ b = 1100
        
        # a = 1110, b = 0010,
        # a & b = 0010, not 0000 so we will now keep the diff bits as first input
        # a = a ^ b = 1100, then a & b = 0010 << 1, becomes b = 0100
        # Hence now a = 1100, b = 0100, a & b is not 0000
        # a = a ^ b = 1000, then a & b = 0100 << 1, becomes b = 1000
        # Now a = 1000, b = 1000, a & b is not 0000
        # a = a ^ b = 0000, then a & b = 1000 << 1, becomes b = 10000
        # Now a & b is 0000 hence return 10000
    
    
        mask = 0xffffffff # (to prevent overflow  in python and stop running into infinite loop, we use 32bit mask to limit int size to 32bit which is much large in python)
        while(b & mask > 0):
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return (a & mask) if b > 0 else a