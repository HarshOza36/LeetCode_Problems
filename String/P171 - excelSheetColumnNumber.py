class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        for c in columnTitle:
            # we do ord(c) minus 64 to get the char in 1-26 range of alphabets
            temp = ord(c) - 64 
            out = out * 26 + temp
        return out