class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low & 1 and high & 1:
            return ((high - low + 1) // 2) + 1
        else:
            return  (high - low + 1) // 2