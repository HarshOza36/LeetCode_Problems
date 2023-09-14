class Solution {
    public int numWays(String[] words, String target) {
        // First for every word we will get count of the charaters at the current index k
        // Next we will loop on the target and check if we can generate the target using
        // the current index characters. Time taken will be O(s * (w+n)), Space O(s+n) where
        // s is length of string, w is length of words array and n is length of target.
        

        long MOD = (long)1000000007;
        int n = target.length();
        long[] dp = new long[n+1];
        dp[0] = 1;

        for(int i = 0; i < words[0].length(); i++){
            int[] count = new int[26];
            for (String w : words) count[w.charAt(i) - 'a']++;

            for (int j = n - 1; j >= 0; j--) {
                // total number of ways forming target uptil j characters will be
                // the count of the current character at k * the previous values
                dp[j+1] += dp[j] * count[target.charAt(j) - 'a'] % MOD;
            }
        }
        return (int)(dp[n] % MOD);
    }
}