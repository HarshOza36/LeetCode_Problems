class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Brute force O(mn) - TLE
#         freq_p = {}
#         for ch in p:
#             if ch in freq_p:
#                 freq_p[ch] += 1
#             else:
#                 freq_p[ch] = 1
        
#         m,n = len(s), len(p)
#         l,r = 0,0
#         # creating a window
#         for _ in range(n-1):
#             r += 1
        
#         output = []
#         while(r < m):
#             freq_curr = {}
#             for i in range(l, r+1):
#                 if(s[i] in freq_curr):
#                     freq_curr[s[i]] += 1
#                 else:
#                     freq_curr[s[i]] = 1
            
#             if(freq_p == freq_curr):
#                 output.append(l)
#             l += 1
#             r += 1
            
#         return output
        # O(n)
        m,n = len(s), len(p)
        
        if(n > m): return []
        
        freq_p, freq_s = {}, {}
        
        # counting all frequencies of p and also the first window
        # because window is always len(p)
        for i in range(n):
            ch_p = p[i]
            if ch_p in freq_p:
                freq_p[ch_p] += 1
            else:
                freq_p[ch_p] = 1
            
            ch_s= s[i]
            if ch_s in freq_s:
                freq_s[ch_s] += 1
            else:
                freq_s[ch_s] = 1
                
        
    
        ans = [0] if freq_p == freq_s else []    

        # comparison of dictionaries runs O(26) worst case because only a-z can be keys
        
            
        l = 0
        for r in range(n, m):
            # adding the character in the right pointer
            if(s[r] in freq_s):
                freq_s[s[r]] += 1
            else:
                freq_s[s[r]] = 1
            
            # After adding right, we will delete left and increment to move window
            # for example s = "cbaed", p = "abc", l= 0,r=3
            # our window before was cba, we add e to it cbae and remove c to get 
            # bae
            
            freq_s[s[l]] -= 1
            if(freq_s[s[l]] == 0): freq_s.pop(s[l]) 
            l += 1 
            if(freq_p == freq_s):
                ans.append(l)
        return ans
