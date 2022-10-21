class Solution:
    def sortString(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        ans = ""
        while len(freq) != 0:
            for i in range(26):
                ch = chr(ord('a') + i)
                if ch in freq:
                    ans += ch
                    freq[ch] -= 1
                    if freq[ch] == 0:
                        freq.pop(ch)
            
            for i in range(26):
                ch = chr(ord('z') - i)
                if ch in freq:
                    ans += ch
                    freq[ch] -= 1
                    if freq[ch] == 0:
                        freq.pop(ch)
        return ans
            
        