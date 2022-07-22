class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        # calculating prefix sum
        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
                
        res = 0
        # i and j are start and end cols respectively
        # we will go row wise and sum in this col range to form 1d array and check 
        # if we found target sum
        
        for i in range(n):
            for j in range(i, n):
                preSums = {0: 1}
                s = 0
                for curr_row in range(m):
                    s += matrix[curr_row][j] - (matrix[curr_row][i-1] if i > 0 else 0)
                    res += preSums.get(s - target, 0)
                    preSums[s] = preSums.get(s, 0) + 1
        return res