class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # We are asked not to use built in methods
        if num1 == '0' or num2 == '0':
            return '0'    
        
        # Turn Each string into numbers
        s1,s2 = num1,num2
        num1,num2 = 0,0
        for i in s1: 
            # Subtract 48 from the current digit 
            num1 = num1 * 10 + (ord(i) - 48) 
        for i in s2: 
            # Subtract 48 from the current digit 
            num2 = num2 * 10 + (ord(i) - 48) 
        
        # Multiply
        final = num1*num2
        
        # Turn back number to string
        final_str = ""
        while True:
            final, remainder = divmod(final, 10)
            final_str = chr(ord('0') + remainder) + final_str
            if final == 0:
                break
                
        return final_str