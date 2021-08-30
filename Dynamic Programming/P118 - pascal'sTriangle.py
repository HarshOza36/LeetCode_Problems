class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        out = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(out[i-1][j-1] + out[i-1][j])
            temp.append(1)
            out.append(temp)
        
        return out