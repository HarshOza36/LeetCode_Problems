class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        int[][] jobs = new int[n][3];

        for(int i = 0; i < n; i++){
            jobs[i] = new int[]{startTime[i], endTime[i], profit[i]};
        }
        // sorting all jobs by endtime
        Arrays.sort(jobs, (a, b)->a[1] - b[1]);

        TreeMap<Integer, Integer> dp = new TreeMap();
        dp.put(0, 0);
        for (int[] job : jobs) {
            // Getting the greatest job less than or equal to the given currJob start
            int curr = dp.floorEntry(job[0]).getValue() + job[2];

            // If this current job profit is largest compared to the max profit
            // we will add the this current job end time with its profit
            if (curr > dp.lastEntry().getValue())
                dp.put(job[1], curr);
        }

        // finally we return the maximum one.
        return dp.lastEntry().getValue();
    }
}