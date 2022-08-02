class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        
        def getFreq(word):
            freq = [0]*26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            return freq
        
        # from the whole words2 we need to get max freq of the chracters
        # in all words of words2
        # for example eoo, oee
        # first word e:1, o:2 and second word o:1, e:2
        # finally we store e:2, o:2
        
        
        B_maxFreq = [0]*26
        
        for w in words2:
            for idx, f in enumerate(getFreq(w)):
                # f is the freq we receive
                B_maxFreq[idx] = max(B_maxFreq[idx], f)
                
        
        # now once we have this max frequencies of words2(B)
        # we will just compare the frequencies of characters in each word
        # for the words1(A) and get our output

        ans = []
        for w in words1:
            A_freq = getFreq(w)
            # we will now check each of frequencies,
            # if we break frequencies dont match
            # if the for loop completes without break , then we append

            for i in range(26):
                if A_freq[i] < B_maxFreq[i]:
                    break
            else:
                ans.append(w)
        return ans   