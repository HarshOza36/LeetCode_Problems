class Solution {
    public int minTaps(int n, int[] ranges) {
        // This is basically like jump game.
        // our range there was index i to i + jump being left and right.
        // Here our left is i - ranges[i] and right is i + ranges[i]
        // so we will create an array which will store this range.
        // to convert this to jump game, we need index i as left and our jump as right.
        // Now say at tap 1, our range is -3, 5 so if -3 is our left, we can make a jump
        // till 5, since array cannot go below 0, we take max(0, -3) as our left
        // and jump as right.

        int res = 0, end = 0, farCanReach = 0;
        int[] reach = new int[n];
        for(int i = 0; i < ranges.length; i++) {
            if(ranges[i] == 0) continue;
            int left = Math.max(0, i - ranges[i]);
            reach[left] = i + ranges[i];
        }

        int i = 0;
        while(end < n){
            res++;
            while(i < reach.length && i <= end){
                farCanReach = Math.max(farCanReach, reach[i++]);
            }

            if(end == farCanReach) return -1;
            end = farCanReach;
        }
        return res;
    }
}