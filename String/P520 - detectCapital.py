class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        for ch in word:
            if ch.isupper(): capitals += 1
        return capitals == 0 or (capitals == 1 and word[0].isupper()) or capitals == len(word)