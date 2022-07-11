class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # Brute Force
        # ans = []
        # n = len(prices)
        # for i in range(n):
        #     j = i + 1
        #     while(j < n):
        #         if(prices[j] <= prices[i]):
        #             ans.append(prices[i] - prices[j])
        #             break
        #         j += 1
        #     else:
        #         ans.append(prices[i])
        # return ans
        
        # Using Monotonic Stack
        stack = []
        ans = prices
        
        for i,n in enumerate(prices):
            while stack and stack[-1][0] >= n:
                (lastNum, idx) = stack.pop()
                ans[idx] = lastNum - n
            stack.append((n,i))
        return ans               