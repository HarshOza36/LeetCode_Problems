class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ("".join([i for i in s if i.isalnum()])).lower()
        return new_s[::-1] == new_s