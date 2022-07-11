class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = {}
        bull, cow = 0, 0
        n = len(secret)
        for ch in secret:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        for i in range(n):
            if(secret[i] == guess[i]):
                bull += 1
                freq[secret[i]] -= 1
            
        for i in range(n):
            if(secret[i] != guess[i] and guess[i] in freq and freq[guess[i]] > 0):
                cow += 1
                freq[guess[i]] -= 1
        return f"{bull}A{cow}B"
        
        