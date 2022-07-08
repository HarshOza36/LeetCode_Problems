class Solution(object):
    def minCost(self, houses, cost, h, c, t):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type h: int
        :type c: int
        :type t: int
        :rtype: int
        """
        inf = 10 ** 20
        dp = [[[None]* (c + 1) for _ in range(t + 1)]for _ in range(h + 1)]
        
        def dfs(idx, target, last_color):
            if(idx >= h or target < 0):
                return target if target == 0 else inf
            if(houses[idx] != 0):# already painted
                if(houses[idx] != last_color):
                    return dfs(idx + 1, target - 1, houses[idx])
                else:
                    return dfs(idx + 1, target, houses[idx])
            if(dp[idx][target][last_color]):
                return dp[idx][target][last_color]
            res = inf
            for clr in range(1, c+1):
                if(clr != last_color):
                    res = min(res, cost[idx][clr-1] + dfs(idx + 1, target - 1, clr))
                else:
                    res = min(res, cost[idx][clr-1] + dfs(idx + 1, target, clr))
            dp[idx][target][last_color] = res
            return res
        res = dfs(0, t, 0)
        return -1 if res >= inf else res