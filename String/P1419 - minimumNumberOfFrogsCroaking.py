class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        freq = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}

        def isValid(freq):
            return freq['c'] >= freq['r'] and freq['r'] >= freq['o'] and freq['o'] >= freq['a'] and freq['a'] >= freq['k']


        frogs = 0
        ans = -1
        for ch in croakOfFrogs:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1    

            if not isValid(freq):
                return -1

            if ch == 'c':
                frogs += 1 
            if ch == 'k':
                frogs -= 1

            ans = max(ans, frogs)
        return ans if frogs == 0 else -1