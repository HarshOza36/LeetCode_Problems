class Solution {
    public int diagonalSum(int[][] mat) {
        int ans = 0;
        int n = mat.length;
        int j =0;
        for(int i = 0; i < n;i++){
                if(j != (n-1-j)) ans = ans + mat[i][j] + mat[i][n -1-j];
                else ans = ans + mat[i][j];
                j += 1;
        }
        return ans;
    }
}