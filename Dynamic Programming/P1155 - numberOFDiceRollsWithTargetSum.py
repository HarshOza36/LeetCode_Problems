class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        d = n
        f = k
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for dice in range(1, d + 1):
            for j in range(dice, target + 1):
                for face in range(1, f + 1):
                    if j - face >= 0:
                        dp[dice][j] += dp[dice - 1][j - face]
        return dp[-1][-1]  % (10 ** 9 + 7)
