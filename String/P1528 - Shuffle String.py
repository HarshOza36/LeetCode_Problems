class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d = dict(zip(indices,s))
        new_s = ""
        for i in range(len(s)):
            new_s += d[i]
        return new_s
            