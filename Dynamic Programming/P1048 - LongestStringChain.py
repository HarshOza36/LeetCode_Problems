class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPredecessor(w1, w2):
            # If the len of precedecessor + 1 is not the new word , return false
            if len(w1) + 1 != len(w2): 
                return False
            # check if word1 is substring of word2
            i = 0
            for c in w2:
                if i == len(w1): 
                    return True
                if w1[i] == c:
                    i += 1
            return i == len(w1)
        
        
        # sorting as per length so always we get prev length greater than new
        words.sort(key=len)
        
        # Now applying longest increasing subsequence
        # Runs in O(N * L^2) where L is length of words which is <= 16
        n = len(words)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if isPredecessor(words[j], words[i]) and (dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
            ans = max(ans, dp[i])
        print(dp)
        return ans