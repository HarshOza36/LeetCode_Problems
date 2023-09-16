class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1),len(word2)
        i, j = 0, 0
        output = []

        while i < m and j < n:
            output.append(word1[i])
            output.append(word2[j])
            i += 1
            j += 1
        
        while i < m:
            output.append(word1[i])
            i += 1
        
        while j < n:
            output.append(word2[j])
            j += 1
        
        return "".join(output)