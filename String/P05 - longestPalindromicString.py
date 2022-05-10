class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # Brute force
        # out = ''  
        # for i in range(len(s)): 
        #     for j in range(len(s), i, -1):  
        #         if len(out) >= j - i:  
        #             break
        #         elif(s[i:j] == s[i:j][::-1]):
        #             out = s[i:j]
        #             break
        # return out
        
        # Using the Expand from center method
        def expand_from_center(s, l, r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return r - l - 1
        
        if(len(s) < 1):
            return ""
        start = end = 0
        for i in range(len(s)):
            len1 = expand_from_center(s, i, i)
            len2 = expand_from_center(s, i, i + 1)
            length = max(len1, len2)
            if(length > end - start):
                start = i - (length - 1) // 2
                end = i + (length)//2
        return s[start : end + 1]