class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        s = sorted(s,key = lambda x: int(x[-1]))
        for i in range(len(s)):
            s[i] = s[i][:-1]
        return " ".join(s)