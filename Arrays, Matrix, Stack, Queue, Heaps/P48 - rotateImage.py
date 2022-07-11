class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        # Flip
        for i in range(len(matrix)):
            matrix[i].reverse()