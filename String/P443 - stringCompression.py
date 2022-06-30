class Solution(object):
    def compress(self, s):
        """
        :type chars: List[str]
        :rtype: int
        """
        compressed = ""
        consecutive_cnt = 0
        i = 0
        for i in range(1, len(s)):
            consecutive_cnt += 1
            if(s[i-1] != s[i]):
                compressed = compressed + s[i-1] + str(consecutive_cnt) if consecutive_cnt > 1 else compressed + s[i-1]
                consecutive_cnt = 0
        # for the final character
        consecutive_cnt += 1
        compressed = compressed + s[i] + str(consecutive_cnt) if consecutive_cnt > 1 else compressed + s[i]
        
        i = 0
        for c in compressed:
            s[i] = c
            i += 1
        return len(compressed)
        
            