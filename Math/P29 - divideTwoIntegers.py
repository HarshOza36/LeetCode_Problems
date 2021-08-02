class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        
        while a >= b:
            temp = b
            mul = 1
            while a>=temp:
                a -= temp
                temp += temp    
                ans += mul
                mul += mul
        if (dividend < 0 and divisor > 0)or (dividend > 0 and divisor < 0):
            ans =- ans
        if ans >= 2**31-1:
            return 2**31-1
        if ans <= -2**31: 
            return -2**31  
        return ans
