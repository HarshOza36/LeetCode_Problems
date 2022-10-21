class Solution:
    def reverseWords(self, s: str) -> str:
        # Brute force Pythonic accepted
        # return " ".join([w[::-1] for w in s.split(" ")])
        
        # Two pointer approach
            
        l, r = 0, 1
        s = list(s)

        while l < len(s)-1 and r < len(s)-1:
            while(r < len(s) and s[r] != " "):
                r += 1
            temp = r
            while(l < temp-1):
                s[l], s[temp-1] = s[temp-1], s[l]
                l += 1
                temp -= 1
            l = r + 1
            r += 1
        return "".join(s)