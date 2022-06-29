class Solution:
    def arrangeCoins(self, n: int) -> int:
      
        # Using math we can find where n lies in sum of m intergers
        # Like m(m+1) / 2 <= n
        # that is m^2 + m <= 2*n
        # adding 1/4 on both sides we get m^2 + m + 1/4  <= 2n + 1/4
        # that is (m + 1/2)^2 <= 2n + 1/4
        # that is m <= sqrt(2n + 1/4) - 1/2
        # return int((2*n + 1/4)**0.5 - (1/2))
    
        # Using Binary Search
        if (n <= 3):
            return 2 if n == 3 else 1
        l = 0
        r = n/2
        while(l <= r):
            mid = (l + r) // 2
            arranged_coins = (mid * (mid + 1)) // 2 # that is n(n+1)/2
            if(arranged_coins == n):
                return int(mid)
            elif(arranged_coins < n):
                l = mid + 1
            else:
                r = mid - 1
        return int(r)
      
      
      
