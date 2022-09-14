class Solution:
    def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         if n == 1:
#             return True
        
#         while n > 1:
#             mod = n % 4
#             if mod != 0:
#                 return False
#             n /= 4
#         return True
        
        # Follow up without loops and recursion
        # check if n > 0 and if last digit of n is 0
        # since all power of 4 are in form 000(4^0), 100(4^1), 10000(4^2)
        # we notice that 1 bits will be in even position for power of 4
        # so we will and n with 0xAAAAAAAA that is 101010..10 (32 bits)
        # so here we are setting all even bits to 0
        # hence if its a power of 4, after AND we should get 0
        return n > 0 and (n & (n-1)) == 0 and (n & 0xAAAAAAAA) == 0