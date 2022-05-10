class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = {}
        n = len(s1)
        found = 0
        for ch in s1:
            if(ch in freq_s1):
                freq_s1[ch] += 1
            else:
                freq_s1[ch] = 1
        
        
        for i in range(len(s2)):
            if s2[i] in freq_s1: 
                freq_s1[s2[i]] -= 1
                if freq_s1[s2[i]] == 0:
                    found += 1
            if i >= n and s2[i-n] in freq_s1: 
                if freq_s1[s2[i-n]] == 0:
                    found -= 1
                freq_s1[s2[i-n]] += 1

            if found == len(freq_s1):
                return True

        return False