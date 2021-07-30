class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            return len(s.split()[-1])
        except Exception as e:
            return 0
