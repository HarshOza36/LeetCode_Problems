class Solution {
    public String kthSmallestPath(int[] destination, int k) {
        // First calculating all paths from origin to destination
        int[][] dp = new int[destination[0] + 1][destination[1] + 1];
        for(int i = 0; i <= destination[0]; i++){
            for(int j = 0; j <= destination[1]; j++) {
                if(i == 0 && j == 0) dp[i][j] = 1;
                else if(i == 0) dp[i][j] = dp[i][j - 1];
                else if(j == 0) dp[i][j] = dp[i - 1][j];
                else dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
            }
        }

        StringBuilder sb = new StringBuilder();
        int i = destination[0], j = destination[1];

        // at every step we choose to go right if previous col of same row has more paths 
        // than k else we will move down.
        while(i != 0 && j != 0) {
            // if k <= the number of paths starting with H
            // hence pick H to move right
            if(dp[i][j - 1] >= k) {
                j--;
                sb.append('H');
            
            }else {
                // otherwise move down and deduct k since we dont have more paths than k
                k -= dp[i][j - 1];
                i--;
                sb.append('V');
            }
            }
            for(int m = 0; m < i; m++) sb.append('V');
            for(int m = 0; m < j; m++) sb.append('H');
            return sb.toString();
    }
}