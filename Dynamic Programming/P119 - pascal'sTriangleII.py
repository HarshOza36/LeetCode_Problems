class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        out = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            temp = [1]
            for j in range(1, i):
                temp.append(out[i-1][j-1] + out[i-1][j])
            temp.append(1)
            out.append(temp)
        
        return out[rowIndex]