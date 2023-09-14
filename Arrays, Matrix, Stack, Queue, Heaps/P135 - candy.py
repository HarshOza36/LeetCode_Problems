class Solution:
    def candy(self, ratings: List[int]) -> int:
        # a 2 pass O(n) time and space solution
        # n = len(ratings)
        # candies = [1] * n
        
        # for i in range(1, n):
        #     if ratings[i] > ratings[i-1]:
        #         candies[i] = candies[i-1] + 1   
        
        # for i in range(n-1, 0, -1):
        #     if ratings[i-1] > ratings[i]:
        #         candies[i-1] = max(candies[i-1], candies[i] + 1)
           
        # return sum(candies)

        # O(n) time O(1) space
        n = len(ratings)
        candies = n
        i = 1
        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            
            peak = 0
            while ratings[i] > ratings[i-1]:
                peak += 1
                candies += peak
                i += 1
                if i == n: return candies
            
            valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                valley += 1
                candies += valley
                i += 1
            
            candies -= min(peak, valley)
        return candies
