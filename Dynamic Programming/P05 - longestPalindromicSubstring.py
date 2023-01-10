class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Using DP
        # say s = abcba then to check if this is palindrome
        # that is substring(start,end) is palindrome
        # if s[start] = s[end] here pointing at both a and
        # letters in between this boundary should also be palindrome
        # that is dp[start+1][end-1] is also palindrome
        # Our initialization will be a single letter that is dp[i][i] is always palindrome
        # And for 2 letters from 0..n we can compare each to see if they are palindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        out = s[0]
        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j] and (i + 1 == j or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if len(out) < j - i + 1:
                        out = s[i:j + 1]
        return out
    
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
#         def expand_from_center(s, l, r):
#             while(l >= 0 and r < len(s) and s[l] == s[r]):
#                 l -= 1
#                 r += 1
#             return r - l - 1
        
#         if(len(s) < 1):
#             return ""
#         start = end = 0
#         for i in range(len(s)):
#             len1 = expand_from_center(s, i, i)
#             len2 = expand_from_center(s, i, i + 1)
#             length = max(len1, len2)
#             if(length > end - start):
#                 start = i - (length - 1) // 2
#                 end = i + (length)//2
#         return s[start : end + 1]

        