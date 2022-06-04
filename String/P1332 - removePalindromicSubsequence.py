class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: 
                break
            l, r = l + 1, r - 1
        else: return 1
        return 2