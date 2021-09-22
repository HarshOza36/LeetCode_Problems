class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l,r = 0,len(s)-1
        while l <= r:
            if(ord(s[l]) in range(65,91) or ord(s[l]) in range(97,123)):
                if(ord(s[r]) in range(65,91) or ord(s[r]) in range(97,123)):
                    s[l],s[r] = s[r],s[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            else:
                l += 1
                
        return "".join(s)
                