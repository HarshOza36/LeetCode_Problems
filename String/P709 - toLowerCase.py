class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s.lower()
        # The problem asks us to use ASCII and not built in functions
        out = ""
        for i in range(0, len(s)):
            if ord(s[i]) in range(65, 91):
            # we can use if s[i].isalnum() but still its built in so we used ascii
                newchar = ord(s[i]) + 32
                out += chr(newchar)
            else:
                out += s[i]
        return out