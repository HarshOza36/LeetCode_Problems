class Solution:
    def isHappy(self, n: int) -> bool:
        def nextSqNum(n):
            total = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                total += digit ** 2
            return total 
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = nextSqNum(n)
        return n == 1