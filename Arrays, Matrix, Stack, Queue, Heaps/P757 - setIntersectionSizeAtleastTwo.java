class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        // First we will sort intervals by end, and on tie by start
        // For each set interval now we need to make decision on which values to add
        // for the first interval we will add the second last and last value of the set
        // Now for the further intervals we can check
        // 1. if the previous added last value = current set start OR if 
        //    secondLast value < start, we can just add current end to cover this set. 
        // 2. otherwise we will again have to add second last and last element of the set.


        Arrays.sort(intervals, (a, b) -> a[1] == b[1] ? a[0]- b[0] : a[1] - b[1]);
        List<Integer> res = new ArrayList();
        res.add(intervals[0][1] - 1);
        res.add(intervals[0][1]);

        for(int i = 1; i < intervals.length; i++){
            int start = intervals[i][0], end = intervals[i][1];
            int secondLast = res.get(res.size()-2), last = res.get(res.size()-1);

            if(start > last){
                res.add(end-1);
                res.add(end);
            }else if(start == last || start > secondLast) res.add(end);

        }
        return res.size();
    }
}