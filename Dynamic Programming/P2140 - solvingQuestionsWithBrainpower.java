class Solution {
    long[] memo;
    public long mostPoints(int[][] questions) {
        memo = new long[questions.length];
        return dp(questions, 0);
    }

    public long dp(int[][] questions, int i){
        if(i >= questions.length) return 0;
        if(memo[i] > 0) return memo[i];
        long solve = dp(questions, i+1+questions[i][1]);
        long dontSolve = dp(questions, i+1);
        memo[i] = Math.max(questions[i][0] + solve, dontSolve);
        return memo[i];
    }
}