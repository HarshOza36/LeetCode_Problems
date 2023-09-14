class Solution {
    public int numSubseq(int[] nums, int target) {
        int MOD = 1000000007, ans = 0, l = 0, r = nums.length - 1;
        Arrays.sort(nums);
        int[] pow = new int[nums.length];
        pow[0] = 1;
        for(int i = 1; i < nums.length; i++){
            pow[i] = pow[i-1] * 2 % MOD;
        }
        while(l <= r){
            if(nums[l] + nums[r] > target){
                r--;
            }else{
                ans = (ans + pow[r-l]) % MOD;
                l++;
            }
        }

        return ans % MOD;
    }
}