class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0:
            return 0
        gcd = self.gcd(p,q)
        p /= gcd
        q /= gcd
        
        if q % 2 == 0:
            return 0
        elif p % 2 == 0:
            return 2
        else:
            return 1
        