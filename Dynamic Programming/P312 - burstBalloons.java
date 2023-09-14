class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] newNums = new int[n+2];
        newNums[0] = 1;
        for(int i = 0; i < n; i++) newNums[i+1] = nums[i];
        newNums[newNums.length-1] = 1;



        int[][] dp = new int[n+2][n+2];
        return dfs(dp, newNums, 1, newNums.length-2);

    }
    public int dfs(int[][] dp, int[] nums,  int l, int r){
        if(l > r) return 0;
        if(dp[l][r] > 0) return dp[l][r];
        
        dp[l][r] = 0;

        for(int i = l; i < r+1; i++){
            int coins = nums[l-1] * nums[i] * nums[r+1];
            coins += dfs(dp, nums, l, i-1) + dfs(dp, nums, i+1, r);
            dp[l][r] = Math.max(dp[l][r], coins);
        }

        return dp[l][r];

    }
}