class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_D = 1
        sum_D = 0
        while n > 0:
            rem = n % 10
            prod_D *= rem
            sum_D += rem
            n //= 10
            
        return prod_D - sum_D
            