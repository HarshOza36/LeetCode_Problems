class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_row = m
        min_col = n
        for x,y in ops:
            min_row = min(min_row, x)
            min_col = min(min_col, y)
        return min_row*min_col