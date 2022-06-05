class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        first_row_zero = False
        
        # to determine which row col need to be zero'd
        # we will use first row and first col as flags to store if they have 
        # zeros. First cell will overlap so we will save it as a row_zero 
        # flag and keep on updating other 0th row and 0th colvalues as per 
        # the matrix
        
        
        for i in range(r):
            for j in range(c):
                if(matrix[i][j] == 0):
                    # First we will set the column value to be zero in first row.
                    matrix[0][j] = 0
                    # Now if its not first row, we will set value to be zero in  first col          
                    if i > 0:
                        matrix[i][0] = 0
                    # if it is first row, will will set our flag
                    else:
                        first_row_zero = True
        
        # zero out everything as per flags in 0th row and col
        for i in range(1, r):
            for j in range(1, c):
                if(matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
                    
        if(matrix[0][0] == 0):
            # that means first column is zero
            for i in range(r):
                matrix[i][0] = 0
                
        if(first_row_zero):
            # that means first row is zero
            for j in range(c):
                matrix[0][j] = 0