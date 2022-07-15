class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        m,n = len(s), len(t)
        if(m < n):
            return ""
        ans = ""
        freq_t = {}
        for ch in t:
            freq_t[ch] = 1 + freq_t.get(ch, 0)
        
        count_t = len(freq_t)
        # we will use this variable so that we dont need to traverse whole dict
        # again and again
        min_len = float('inf')
        for r in range(m):
            if(s[r] in freq_t):
                freq_t[s[r]] -= 1
                if(freq_t[s[r]] == 0):
                    count_t -= 1
            if count_t == 0:
                while count_t == 0:
                    if len(s[l:r+1]) < min_len:
                        ans = s[l:r+1]
                        min_len = len(s[l:r+1])
                    if s[l] in freq_t:
                        freq_t[s[l]] += 1
                        if(freq_t[s[l]] > 0):
                            count_t += 1
                    l += 1 
        return ans