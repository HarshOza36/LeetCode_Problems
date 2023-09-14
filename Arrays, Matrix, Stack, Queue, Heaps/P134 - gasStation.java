class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // Firstly, if the total gas sum is smaller than cost sum, its never possible to 
        // come back to start, because we wont have that much gas
        // Once we confirm that there is a possible start, we will then check the
        // difference of gas - cost at each index.
        // for gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        // diff = [-2, -2, -2, 3, 3]
        // Now we will start adding the diff values to a variable say total
        // at any point, if the total < 0 at i that means, we ran out of gas at that position
        // hence we set the start point to its next index i+1.
        // This is greedy, we will try the next position, if the total is positive, we go on
        // as soon as again we go < 0, we will go to i+1th position.
        //  when we reach the end of the array, we dont need to go back to start, 
        // because we verified sum(gas) >= sum(cost) hence whatever start was found 
        // that will be our answer.

        int gasSum = 0, costSum = 0, start = 0;

        for(int g: gas) gasSum += g;
        for(int c: cost) costSum += c;
        if(gasSum < costSum) return -1;

        int total = 0;

        for(int i = 0;  i < gas.length; i++){
            total += gas[i] - cost[i];
            if(total < 0){
                total = 0;
                start = i + 1;
            }
        }

        return start;
        
    }
}