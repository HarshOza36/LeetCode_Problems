class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if(ch in freq):
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        out = ""

        for k,v in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            out += (k * v)
        
        return out