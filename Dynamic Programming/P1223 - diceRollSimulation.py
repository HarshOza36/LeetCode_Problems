class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        # we need to create a 3d dp where
        # i is the number of dice n
        # j is fixed 6 numbers that dice can roll
        # k will be the constraint of consecutive occurence from 1-15 as given
        
        # Time complexity of this will be
        # O(n * 6 * 15 * 6 * 15) that is O(n)
        dp  = [[[0]*16 for _ in range(6)] for _ in range(n)]
        
        # initializing dp
        # when we roll dice just once
        for i in range(6):
            dp[0][i][1] = 1
        
        
        for i in range(1, n):
            for j in range(6):
                for k in range(1, rollMax[j]+ 1):
                    if k > 1:
                        # this means like we can have this consecutive j
                        # value so we can copy it from previous occurence
                        dp[i][j][k] = dp[i-1][j][k-1]
                    else:
                        # that means it will be equal to one
                        # so we cannot take the same j
                        # we will have to take all the other options 
                        # and add to it.
                        for jj in range(6):
                            for kk in range(1, rollMax[jj] + 1):
                                if j == jj:
                                    continue
                                # if the j is not same, then we will
                                # add the combination to current i.j.k
                                dp[i][j][k] += dp[i-1][jj][kk]
        
        # finally we will take sum of the last row of dp to get our output 
        # possible combination.
        
        out = 0
        for j in range(6):
            for k in range(1, rollMax[j] + 1):
                out += dp[-1][j][k]
        return out % MOD