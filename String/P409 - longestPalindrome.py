class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 1:
            return n
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
        cnt = 0
        for v in freq.values():            
            cnt += v//2 * 2
            if(cnt % 2 == 0 and v % 2 == 1):
                cnt += 1
        return cnt