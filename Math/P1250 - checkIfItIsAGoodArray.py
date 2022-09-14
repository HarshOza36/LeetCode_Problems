class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Using the Hint
        # Idea is that for a and b, if gcd(a,b) = c, then there exist 
        # x and y, such that a*x + b*y = c

        # This can be also be generalized
        # if gcd(a,b,c) = d, then there exist integers x, y, and z 
        # such that, a*x + b*y + c*z = d
        
        # we know gcd is commutative and associative.
        # Hence to solve this problem we find IF gcd(a1,a2 ... an) = 1
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        gcd_val = nums[0]
        for i in range(1, len(nums)):
            gcd_val = gcd(gcd_val, nums[i])
            if(gcd_val == 1):
                return True
        return gcd_val == 1