class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []

        def backtrack(idx, word, spaces):
            if idx == len(s) and (len(word) - spaces) == len(s):
                ans.append(word[1:])
                return

            if idx > len(s):
                return
            
            for w in wordDict:
                if (idx + len(w)) <= len(s):
                    brokenWord = s[idx : idx + len(w)] 
                    if brokenWord == w:
                        backtrack(idx + len(w), word + ' ' + brokenWord, spaces + 1)
                    
            backtrack(idx + 1, word, spaces)
            
        backtrack(0, '', 0)
        return ans