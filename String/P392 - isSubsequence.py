class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(t) == 0):    
            return False if(len(s) != 0) else True
        l = 0 
        r = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1    
            r += 1
        if l < len(s) and s[l] == t[r-1]:
            l += 1    
        if(l == len(s)):
            return True
        return False