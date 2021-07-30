class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(len(needle) == 0):
            return 0
        else:
            return haystack.find(needle)