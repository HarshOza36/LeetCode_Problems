class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # brute force
##        if(str(x) == str(x)[::-1]):
##            return True
##        else:
##            return False
        # math
        if x < 0:
            return False
        num = 0
        temp = x
        while x:
            r = x % 10
            x = x // 10
            num = (num * 10) + r
        
        return num == temp
                    
