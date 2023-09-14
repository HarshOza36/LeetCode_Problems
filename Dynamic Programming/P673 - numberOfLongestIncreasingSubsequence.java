class Solution {
    public int findNumberOfLIS(int[] nums) {
        Map<Integer, int[]> dp = new HashMap();
        // dp[i] will store maxLen of lis and maxCount of lis that we can form at index i.
        int lisLen = 0, res = 0, n = nums.length;

        for(int i = n-1; i >= 0; i--){
            int maxLen = 1, maxCnt = 1;
            for(int j = i+1; j < n; j++){
                if(nums[j] > nums[i]){
                    int len = dp.get(j)[0];
                    int count = dp.get(j)[1];
                    if(len+1 > maxLen){
                        maxLen = len+1;
                        maxCnt = count;
                    }else if(len+1 == maxLen){
                        // found another subsequence of same maxLen
                        maxCnt += count;
                    }
                }
            }
            if(maxLen > lisLen){
                lisLen = maxLen;
                res = maxCnt;
            }else if(maxLen == lisLen){
                res += maxCnt;
            }
            dp.put(i, new int[]{maxLen, maxCnt});

        }
        return res;
    }
}