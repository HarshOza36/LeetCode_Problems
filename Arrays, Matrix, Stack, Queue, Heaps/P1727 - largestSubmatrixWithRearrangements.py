class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # TC O(mnlogn)
        # basically it is finding max rectangle in sorted histogram structure
        # but with broken histogram pillars

        # we will iterate every pillar and find the max rectangle while considering the
        # rows. For the rows, if we find a broken pillar as 101 we will ignore that 
        # whole column of pillar itself.
        # for that when traversing each rows we will check row above  and then we check
        # if a broken pillar is forming, so if at any point we get 0 going down the matrix
        # we will make the whole pillar as zero, while for others we will be adding the 1
        # and then at each level sort the row, to find max rectangle
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            curr = sorted(matrix[i], reverse=True) 

            for k in range(n):
                ans = max(ans, curr[k] * (k + 1))
        
        return ans