class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        wealths = []
        for cust in accounts:
            cust_wealth = sum(cust)
            wealths.append(cust_wealth)
        return max(wealths)
                
                