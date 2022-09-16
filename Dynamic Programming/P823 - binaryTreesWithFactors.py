class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(arr)
        # we sort the array so that, we can compare the numbers
        # in ascending and then use division
        arr.sort()
        
        dp = [1] * n
        index = {x: i for i, x in enumerate(arr)}
        
        for i, x in enumerate(arr):
            # we will run j till i
            # because we wont be able to divide a number and get remainder 
            # 0 if denominator > numerator.
            for j in range(i):
                if x % arr[j] == 0: # arr[j] will be left child
                    # if remainder is zero, we get the left child
                    # and right child will simply be the quotient
                    right = x / arr[j]
                    if right in index:
                        # now to dp[i] we will add
                        # number of ways of forming arr[j]
                        # and multiply it with number of ways of forming
                        # arr[right] which we just found
                        # we need right's index, which we will take from 
                        # our dictionaty
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= mod
        return sum(dp) % mod