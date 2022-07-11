class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        r_start,r_end = 0, len(matrix) - 1
        c_start,c_end = 0, len(matrix[0]) - 1
        while((r_start <= r_end) and (c_start <= c_end)):
            
            # first row
            for c in range(c_start,c_end+1):
                answer.append(matrix[r_start][c])
            r_start += 1
            
            # last column
            for r in range(r_start,r_end+1):
                answer.append(matrix[r][c_end])
            c_end -= 1
            
            if(c_start > c_end or r_start > r_end):
                break
            
            # last row
            for c in range(c_end,c_start-1,-1):
                answer.append(matrix[r_end][c])
            r_end -= 1
            
            # first column
            for r in range(r_end,r_start-1,-1):
                answer.append(matrix[r][c_start])
            c_start += 1
        return answer
