class Solution {
    public int videoStitching(int[][] clips, int time) {
        int res = 0, end = 0, farCanReach = 0, n = clips.length;
        Arrays.sort(clips, (a, b) -> (a[0] - b[0]));
        int i = 0;
        while(end < time){
            res++;
            while(i < n && clips[i][0] <= end){
                // checking all the elements in the range
                farCanReach = Math.max(farCanReach, clips[i][1]);
                i++;
            }
            // if the farCanReach isnt updated even after traversing the full array
            // we cannot further reach ahead hence return -1;
            if(end == farCanReach) return -1;
            // otherwise new end will be farCanReach
            end = farCanReach;
        }
        return res;
    }
}