class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_mag = {}
        for ch in magazine:
            if ch in freq_mag: freq_mag[ch] += 1
            else: freq_mag[ch] = 1
        
        i = 0
        while i < len(ransomNote):
            ch = ransomNote[i]
            if ch in freq_mag and freq_mag[ch] != 0:
                freq_mag[ch] -= 1
            else:
                return False
            i += 1
        return True