class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        n = len(s)
        # Accumulating the shift values
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            
        out = ""
        for i in range(len(s)):
            out += chr((ord(s[i]) + shifts[i]- 97) % 26 + 97)
        return out