class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:      
        # Dp gives tle 28/40
        # n = len(cardPoints)
        # dp = [[0]*(k+1) for i in range(n+1)]
        
        # for i in range(k-1,-1,-1):
        #     for j in range(i, -1,-1):
        #         # we take left path and then right path        
        #         path1 = cardPoints[j] + dp[i+1][j+1]
        #         path2 = cardPoints[(n-1)-(i-j)] + dp[i+1][j]
        #         dp[i][j] = max(path1, path2)
        # return dp[0][0]

        # Sliding window approach
        res = 0
        n = len(cardPoints)
		
		# First k elements in our window
        for i in range(k): 
            res += cardPoints[i]

        
        # Now our window is removing the left side element
        # and adding the right side element as a window
        # so if we had cardPoints = [1,2,3,4,5,6,1], k = 3
        # first our window is 1,2,3
        # then next our window will be 1,2 and 1
        # next window 1 and 6,1
        # finally 5,6,1
        # we will keep taking maximum score at each iteration

        window = res
        for i in range(k-1, -1, -1):	
            window -= cardPoints[i]
            window += cardPoints[n - k + i]
            res = max(res, window)
        return res
    