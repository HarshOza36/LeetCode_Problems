class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            # keeping track of max frequency so we dont need to keeping finding it
            # for the while loop ahead
            maxf = max(maxf, freq[s[r]])
            
            while (r - l + 1) - maxf > k:
                # we will shrink the window if window leng - max freq element exceeds k
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res