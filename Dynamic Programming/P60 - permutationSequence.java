class Solution {
    public String getPermutation(int n, int k) {
        // First given a number n we know we can have n! permutations.
        // Now at every index of the final string, we need to find a number
        // such that it will be our kth permutation.
        // If we had 123, 132, 213, 231, 312, 321 with k = 3, we know answer is 213.
        // First, to get the first index correct, we will divide our permutations in blocks
        // Now how are the blocks divided, we see for first index we have 1 1 2 2 3 3,
        // we see we have 3 blocks 11, 22, 33. Each block has a size 2, its basically (n-1)!
        // Why do we need blocks? so that we can directly see where the kth permutation lies.
        // for k = 3, we know that it will be in block 2, since we have 3 blocks of size 2.

        // Now to get the exact digit, we can simply divide k/(n-1)! + 1
        // Here if we see k = 3 we get 3/2 + 1 = 2
        // for example if k was 4 instead 4/2 + 1 = 3 

        // Once we get the digits, we will up one index in the string.
        // now since we filled that space up, we need to change k as well.
        // to change k, we will to subtract the (k/(n-1)!) * (n-1)!
        // By doing this, we are moving ahead a digit in the final string



        // Calculating Factorials.
        int[] fact = new int[n+1];
        fact[0] = 1;
        for(int i = 1;i< fact.length;i++) fact[i] = fact[i-1]*i;



        boolean[] isOccupied = new boolean[n+1]; //align digit to index
        StringBuilder sb = new StringBuilder();
        k--; // getting K in 0 indexing
        for(int i = n-1;i >= 0;i--){  // Runs O(n)
            //digit(i) = (k-1)/(i-1)! + 1.
            int digit = k/fact[i] + 1;          
            for(int j = 1,count = 0;j <= n;j++){ // Runs O(9) times
                //start from index 1
                if(!isOccupied[j]) count++;
                if(count == digit) {
                    sb.append(j);
                    isOccupied[j] = true;
                    break;
                }
            }

            k -= fact[i]*(k/fact[i]);
        }
        return sb.toString();
    }
    
}