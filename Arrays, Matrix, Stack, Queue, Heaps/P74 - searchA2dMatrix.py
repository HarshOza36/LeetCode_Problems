class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix[0])
        n = len(matrix)
        l = 0
        r = (m*n) - 1
        while(l <= r):
            mid = (l + r) // 2
            mid_row = mid// m
            mid_col = mid % m
            if(matrix[mid_row][mid_col] == target):
                return True
            elif(matrix[mid_row][mid_col] > target):
                r = mid - 1
            else:
                l = mid + 1
        return False