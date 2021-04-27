class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        out = 0
        for i in range(len(costs)):
            if(costs[i]<=coins):
                coins -= costs[i]
                out += 1
        return out
