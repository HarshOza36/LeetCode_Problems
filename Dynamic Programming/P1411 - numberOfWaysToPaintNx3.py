class Solution:
    def numOfWays(self, n: int) -> int:
        
#         a = ["121", "212", "312", "123", "213", "313", "131", "231", "321", "132", "232" ,"323"]
#         # a is the lvl1
#         n2 ={i:[] for i in range(12)}
#         for i in range(len(a)):
#             for j in range(len(a)):
#                 if i == j:
#                     continue
#                 val1, val2 = a[i], a[j]

#                 if not(val1[0] == val2[0] or val1[1] == val2[1] or val1[2] == val2[2]):
#                     n2[i].append(j)
        # generating level2 combination using above code that is n=2
        MOD = 10**9 + 7
        
        lvl2 = {0: [1, 2, 4, 5, 10], 1: [0, 3, 6, 8, 11], 2: [0, 3, 6, 7], 3: [1, 2, 7, 10], 4: [0, 6, 8, 9], 5: [0, 6, 7, 9, 10], 6: [1, 2, 4, 5, 11], 7: [2, 3, 5, 11], 8: [1, 4, 9, 10], 9: [4, 5, 8, 11], 10: [0, 3, 5, 8, 11], 11: [1, 6, 7, 9, 10]}

        
        # This lvl2 gives us the compatibility of each 1x3 combination
        # so we can take the 1x3 block and combine it with its compatible 
        # blocks that is say 0th scenario 121 is compatible with
        # 2nd scenario 312
        dp = [[0]*12 for _ in range(n)]
        
        for i in range(12):
            dp[0][i] = 1
            # since we have 12 combinations
        
        for i in range(1, n):
            for j in range(12):
                for ele in lvl2[j]:
                    # we will increment the compatible combination 
                    # with its parent combination's value
                    dp[i][ele] += dp[i-1][j]
                    dp[i][ele] %= MOD
                    
        return sum(dp[-1]) % MOD
            

        
        