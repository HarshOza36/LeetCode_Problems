class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time complexity O(n^2 . m) where n is length of s and m is length of wordDict
        
        # we will start checking each word if it is there in the string s or not
        # and then we will match first characters say we had leetcode and leet will
        # match first 4
        # then we will again check all the words of word dict and check next sub
        # problem for code
        
        # we will go in reverse order. once we reach the start from end
        # every time we will form some indexes as true because starting from those
        # indexes we will get a word in wordDict
        # finally we return start
        
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s), -1, -1):
            for w in wordDict:
                # we check if the word is in bounds and then compare the word
                if (i + len(w)) <= len(s) and s[i : i+ len(w)] == w:
                    # we will just check after breaking what is the value
                    # of next word
                    # that is leet = dp[index of "c"] for code
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]