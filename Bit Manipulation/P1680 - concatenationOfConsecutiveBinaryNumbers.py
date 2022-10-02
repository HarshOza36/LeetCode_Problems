class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # at each level
        # we will multiply old number with the length of the binary string
        # shifted to right and add the current number
        
        # if we had 
        # 110 = 1 * 100 + 10(2) - here len(10) == 2, 1<<2 = 100
        # 11011 = 110 * 100 + 11(3) 
        # 11011100 = 11011 * 1000 + 100(4) - here len(100) == 3, 1<<3 = 1000
        
        ans = 0
        mod = (10**9 + 7)
        for num in range(n):
            ans = (ans * (1 << (len(bin(num+1)) - 2)) + num+1) % mod
        return ans % mod