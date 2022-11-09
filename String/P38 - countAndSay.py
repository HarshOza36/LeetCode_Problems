class Solution:
    def countAndSay(self, n: int) -> str:
        def compressString(s):
            # Basically Leetcode 443
            compressed = ""
            consecutive_cnt = 0
            i=0
            for i in range(1, len(s)):
                consecutive_cnt += 1
                if(s[i-1] != s[i]):
                    compressed += str(consecutive_cnt) + s[i-1] 
                    consecutive_cnt = 0
            consecutive_cnt += 1
            compressed += str(consecutive_cnt) + s[i]
            return compressed
            
            
        def say(n):
            if n == 1:
                return "1"
            s = say(n-1)
            return compressString(s)
        return say(n)