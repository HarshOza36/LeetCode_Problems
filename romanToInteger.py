class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym_val = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        l = [sym_val[i] for i in s]
        for i in range(0,len(l)-1):
                if l[i]<l[i+1]:
                        l[i] = -l[i]     
        return sum(l)        
            
           