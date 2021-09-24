class Solution:
    def __init__(self):
        self.tribo = {0:0,1:1,2:1}
    def tribonacci(self, n: int) -> int:
        if(n in self.tribo):
            return self.tribo[n]
        else:
            res = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
            self.tribo[n] = res
        return res