class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = {}
        same_letter = cnt = 0
        for w in words:
            # if same_letter
            if w[0] == w[1]:
                # if another same_letter pair exists we add them to count 
                if w in freq and freq[w] > 0:
                    same_letter -= 1
                    freq[w] -= 1
                    cnt += 4
                else: 
                    freq[w] = 1 + freq.get(w, 0)
                    same_letter += 1
            else:
                # if not same letter , we search reverse of it in dictionary
                rev = w[::-1]
                if rev in freq and freq[rev] > 0:  
                    cnt += 4
                    freq[rev] -= 1
                else: 
                    freq[w] = 1 + freq.get(w, 0)
        # if there are same letter remaining then add to cnt
        if same_letter > 0: 
            cnt += 2
        return cnt