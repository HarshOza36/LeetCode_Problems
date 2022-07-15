class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Brute Force
##        n,l,r = len(s),0,0
##        seen = dict()
##        max_len = float('-inf')
##        while r < n:
##            seen[s[r]] = 1 + seen.get(s[r], 0)
##            window_len = r - l + 1
##            if(len(seen) == window_len):
##                max_len = max(max_len, window_len)
##            elif(len(seen) < window_len):
##                while(len(seen) < window_len):
##                    seen[s[l]] -= 1
##                    if(seen[s[l]] == 0):
##                        seen.pop(s[l])
##                    l += 1
##                    window_len = r - l + 1
##                if(len(seen) == window_len):
##                    max_len = max(max_len, r - l + 1) 
##            r += 1
##        return 0 if max_len == float('-inf') else max_len
        
        # Using set
##        seen = set()
##        i = j = max_len = 0
##        while i < len(s):
##            ch = s[i]
##            if ch not in seen:
##                seen.add(ch)
##                i += 1
##            else:
##                seen.remove(s[j])   
##                j += 1
##            max_len = max(max_len,i - j)        
##        return max_len
        
        l, max_len, seen = 0, 0, {}
        for r in range(len(s)):
            ch = s[r]
            if ch in seen:
                l = max(l, seen[ch] + 1)
            seen[ch] = r
            max_len = max(max_len, r - l + 1)
        return max_len
