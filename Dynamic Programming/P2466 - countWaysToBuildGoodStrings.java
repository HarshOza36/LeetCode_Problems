class Solution {
    public int countGoodStrings(int low, int high, int zero, int one) {
        int MOD = 1000000007, ans = 0;
        int[] dp = new int[high+1];
        dp[0] = 1;
        // dp[i] gives length of string at index i
        // for example at i = 1 with low = high = 3 and zero = one = 1
        // we can form 0, 1 (since we can use either 1 zero or 1 one)
        // at i = 2 we can form 00, 01, 10, 11 (on the previous level numbers we can add a 1 or 0 to each possibility)
        // at i = 3 we can form 000, 001, 010, 011, 100, 101, 110, 111 
        // and so on.

        // Finally to get the answer in range low to high, we can check all the possibilities
        // that we can form in that range using this zero and one combinations.
        for(int i = 1; i <= high; i++){
            if(i-zero >= 0) dp[i] = (dp[i] + dp[i-zero]) % MOD;
            if(i-one >= 0) dp[i] = (dp[i] + dp[i-one]) % MOD;
        }
        for(int i = low; i <= high; i++) ans = (ans + dp[i]) % MOD;
        return ans % MOD;
    }
}