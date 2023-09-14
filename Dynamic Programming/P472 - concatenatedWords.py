class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Bruteforce
        # wordSet = set(words)
        # def wordBreak(s):
        #     n = len(s)
        #     dp = [False] * (n+1)
        #     dp[len(s)] = True
            
        #     for i in range(len(s), -1, -1):
        #         for w in wordSet:
        #             if (i + len(w)) <= len(s) and s[i : i+ len(w)] == w and s[i:i+len(w)] != s:
        #                 # we just added extra check here in wordbreak
        #                 # that string formed is not equal to input string to func
                    
        #                 dp[i] = dp[i + len(w)]
        #             if dp[i]: break
        #     return dp[0]
        
        # ans = []
        # for word in words:
        #     if word and wordBreak(word):
        #         ans.append(word)
        # return ans



        # wordSet = set(words)
        # ans = []
        # for word in words:
        #     w = len(word)
        #     dp = [False] * (w+1)
        #     dp[0] = True
        #     for i in range(1, w+1):
        #         j = 1 if i == w else 0
        #         while not dp[i] and j < i:
        #             dp[i] = dp[j] and word[j:i] in wordSet
        #             j += 1
        #     if dp[w]:
        #         ans.append(word)
        # return ans


        # Simple Dfs approach
        words = set(words)
        def dfs(word):
            for i in range(1, len(word)):
                prefix, suffix = word[:i], word[i:]
                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
            return False
        return [word for word in words if dfs(word)]