class Solution:
    def numOfWays(self, n: int) -> int:
        # Generating Lvl1 and Lvl2 then using lvl2 compatability with others
        # R = 1, Y = 2, G = 3
        # lvl1 = [
        #         "121", "212", "312",
        #         "123", "213", "313",
        #         "131", "231", "321",
        #         "132", "232", "323"
        # ]
        # MOD = 10 ** 9 + 7
        # lvl2 = defaultdict(list)
        # for i in range(len(lvl1)):
        #     for j in range(len(lvl1)):
        #         if i != j:
        #             v1 = lvl1[i]
        #             v2 = lvl1[j]
        #             if not(v1[0] == v2[0] or v1[1] == v2[1] or v1[2] == v2[2]):
        #                 lvl2[i].append(j)


        # dp = [[0] * 12 for i in range(n)]
        # for i in range(12):
        #     dp[0][i] = 1
        # for i in range(1, n):
        #     for j in range(12):
        #         for v in lvl2[j]:
        #             dp[i][v] += dp[i-1][j]
        #             dp[i][v] %= MOD
        # return sum(dp[-1]) % MOD


        # Smart Intuition @lee215
        # So we notice there are 2 kinds of patterns that is XYX and XYZ
        # for lvl1 we see XYX is 121, 131, 2122, 232, 313, 323
        # for XYZ we have 123, 132, 213, 231, 312, 321
        # so we have 6 of each XYZ and XYX.
        # For lvl2, since we cant have adjacent same for XYX we can have XYZ and YXY type patterns
        # that is if we have 121, we can have 212, 213, 232, 312, 313
        # same if we have 123, we can have 212, 231, 312 and 232
        # this means we have for XYX we have total 5 - 3 of XYX like and 2 of XYZ
        # and for XYZ we have 4 - 2 of each XYX and XYZ
        # so our dp will be
        # XYX = XYX * 3 + XYZ * 2
        # XYZ = XYX * 2 + XYZ * 2
        # when both are initialized as 6
         
        xyx, xyz, MOD = 6, 6, 10**9 + 7
        for i in range(n - 1):
            xyx, xyz = xyx * 3 + xyz * 2, xyx * 2 + xyz * 2
        return (xyx + xyz) % MOD