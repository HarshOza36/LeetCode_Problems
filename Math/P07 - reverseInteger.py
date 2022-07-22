class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Brute force
#         num = x
#         x = str(abs(x))
#         out = int(x[::-1])
#         if(out > 2**31 -1 or out < -2**31):
#             return 0
#         elif(num < 0):
#             return -1*out
#         else:
#             return out
        
        mul = -1 if x < 0 else 1
        ans = 0
        x = abs(x)
        while x:
            rem = x % 10
            x = x // 10
            ans = ans*10 + rem
        ans = ans * mul
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        else: return ans
