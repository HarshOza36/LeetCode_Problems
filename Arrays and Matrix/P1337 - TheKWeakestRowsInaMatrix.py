class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        vals = {}
        for i in range(len(mat)):
            l = 0
            r = len(mat[i]) - 1
            
            while(l <= r):
                if(mat[i][l] == mat[i][r] == 0): # all zeros in the range
                    vals[i] = 0
                    break
                elif(mat[i][l] == mat[i][r] == 1): # all ones in the range
                    vals[i] = len(mat[i][l:r+1])
                    break
                else:
                    mid = (l + r) // 2
                    if(mat[i][mid] == 0):
                        r = mid - 1
                    else:
                        r -= 1
        vals = sorted(vals.items(), key=lambda x: x[1])
        ans = [v[0] for v in vals[:k]]
        return ans
            