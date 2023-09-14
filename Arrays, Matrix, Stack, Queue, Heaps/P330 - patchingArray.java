class Solution {
    public int minPatches(int[] nums, int n) {
        // while we dont reach n
        // we will keep checking the numbers we have seen.
        // if the number is in the array and we can make next sum we just add it to a currSum that can be formed
        // otherwise we will add the next number in the sum, and patch the array.
        // For example. when we have [1,5,10] and n = 20
        // first we get 1 from array then next we have a 2 to be added, not present in array
        // when we patch 2, we have currSum = 3, because we can form 3, hence now we have 1,2,3 which can be fornmed
        // next we directly have 4 since 3 can be formed. now again 4 will be added and patched. and currSum will be
        //7 since 4+3 is 7 and we can now form 1,2,3,4,5,6,7 next we can directly add a 5 from array and currSum
        // that can be formed will be 12, finally we can directly add 10 to form currrSum 22, since before we 
        // were forming 1..12 now as soon as we add 10, we can use other numbers to reach 20.
        long currSum = 0;
        int ans = 0;
        int i = 0;
        while(currSum < n){
            if(i >= nums.length || nums[i] > currSum+1){
                currSum += currSum + 1;
                ans += 1;
            }else{
                currSum += nums[i++];
            }
        }
        return ans;
    }
}