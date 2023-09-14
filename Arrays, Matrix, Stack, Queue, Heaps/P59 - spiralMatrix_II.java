class Solution {
    public int[][] generateMatrix(int n) {
        int r_start = 0, r_end = n-1, c_start = 0, c_end = n-1;
        int[][] mat = new int[n][n];
        int num = 1;
        while(r_start <= r_end && c_start <= c_end){
            for(int c = c_start; c < c_end + 1; c++){
                mat[r_start][c] = num;
                num++;
            }
            r_start++;

            for(int r = r_start; r < r_end + 1; r++){
                mat[r][c_end] = num;
                num++;
            }
            c_end--;

            if(r_start > r_end || c_start > c_end) break;

            for(int c = c_end; c >= c_start; c--){
                mat[r_end][c] = num;
                num++;
            }
            r_end--;

            for(int r = r_end; r >= r_start; r--){
                mat[r][c_start] = num;
                num++;
            }
            c_start++;
        }
        return mat;

    }
}