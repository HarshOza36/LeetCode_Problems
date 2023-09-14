class Solution {
    public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {
        // Gives TLE
        // int n = obstacles.length;
        // int[] dp = new int[n];
        // dp[0] = 1;
        // for(int i = 1;i < n;i++){
        //     int currMax = Integer.MIN_VALUE;
        //     for(int j = 0;j < i;j++){
        //         if(obstacles[i] >= obstacles[j]){
        //             currMax = Math.max(dp[j] + 1, currMax);
        //         }
        //     }
        //     dp[i] = currMax == Integer.MIN_VALUE ? 1 : currMax;
        // }
        // return dp;

        int i = -1, cur = 0, lisSize = -1;
        int[] lis = new int[obstacles.length];
        int[] ans = new int[obstacles.length];
        
        for (int num: obstacles) {
            if (i == -1 || lis[i] <= num) {
                // If the number is in the increasing sequence
                // just add that number. Current lisSize will be till that index.
                lis[++i] = num;
                lisSize = i;
            } else {
                // otherwise find the leftmost index of where this number
                // can be added. Current lisSize will be this new position.
                lisSize = search(lis, 0, i, num);
                lis[lisSize] = num;
            }
            ans[cur++] = lisSize + 1;
        }
        return ans;      
    }
    
    public int search(int[] nums, int left, int right, int target) {
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) right = mid;
            else left = mid + 1;
        }
        return left;
    }
}