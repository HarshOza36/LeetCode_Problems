class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # sorting by width
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        n = len(envelopes)
        
        # applying LIS on height now.
        # Below O(n^2) gives TLE
        # dp = [0 for i in range(n)]
        # overall_max = 0
        # for i in range(len(dp)):
        #     max_val = 0
        #     for j in range(i):
        #         # If they can fit  
        #         if(envelopes[j][1] < envelopes[i][1] and envelopes[j][0] < envelopes[i][0]):
        #             max_val = max(max_val, dp[j])
        #     dp[i] = max_val + 1
        #     overall_max = max(overall_max, dp[i])
        # return overall_max
        
        # Using Binary search to get LIS on heights
        res = []		
        for _, h in envelopes:
            l, r = 0, len(res)-1
			
            # find the insertion point for height in the Sort order
            # instead of this loop we can directly use bisect_left
            while(l <= r):
                mid = (l + r) // 2
                if(res[mid] >= h):
                    r = mid - 1
                else:
                    l = mid + 1
            idx = l
            if(idx == len(res)):
                res.append(h)
            else:
                res[idx] = h
        return len(res)