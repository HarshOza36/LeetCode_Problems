class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        diags = defaultdict(list)
        
        for i in range(r):
            for j in range(c):
                diags[i-j].append(mat[i][j])
        
        for k in diags.keys():
            diags[k].sort(reverse = True)
            
        for i in range(r):
            for j in range(c):
                mat[i][j] = diags[i-j].pop()
        return mat