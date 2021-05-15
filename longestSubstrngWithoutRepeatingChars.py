class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = []
        out = 0
        maxL = 0
        if(len(s) == 0):
            return 0
        elif(len(s) == len(set(s))):
            return (len(s))
        else:
            for char in s:
                if char not in unique:
                    unique.append(char)
                    out += 1
                else:
                    idx = unique.index(char)
                    unique = unique[idx+1:]
                    unique.append(char)
                    out = len(unique)
                if maxL < out:
                    maxL = out
            return maxL
