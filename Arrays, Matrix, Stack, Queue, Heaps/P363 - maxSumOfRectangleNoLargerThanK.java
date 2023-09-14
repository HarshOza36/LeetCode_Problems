class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        // For followup if we have more rows than columns, we can transpose our 
        // matrix to get complexity O(min(m,n)^2 max(m,n) log(max(m,n)))
        
        int m = matrix.length, n = matrix[0].length;
        int ans = Integer.MIN_VALUE;
        // Runs O(m^2 * nlogn)
        for(int i = 0; i < m; i++){
            int[] arr = new int[n];
            // arr[i] is the sum of matrix[i][x] to matrix[j][x]
            // where i is first row, j is second row and x is the column
            for(int j = i; j < m; j++){
                for(int x = 0; x < n; x++) arr[x] += matrix[j][x];
                ans = Math.max(ans, maxSubArraySumLTK(arr, n, k));
            }
        }
        return ans;
    }
    public int maxSubArraySumLTK(int[] arr, int n, int k){
        TreeSet<Integer> bst = new TreeSet();
        bst.add(0);
        int ans = Integer.MIN_VALUE;
        for(int i = 0, r = 0; i < n; i++){
            r += arr[i];
            // now least element in bst >= r-k or null
            Integer l = bst.ceiling(r - k);
            if(l != null){
                ans = Math.max(ans, r - l);
            }
            bst.add(r);
        }
        return ans;
    }
}