# b1 - bought stock once
# s1 - bought stock and then sold once
# b2 - bought stock the second time
# s2 - bought and sold twice

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = s1 = b2 = s2 = float('-inf')
        for p in prices:
            b1, s1, b2, s2 = max(b1,  - p), max(s1, b1 + p), max(b2, s1 - p), max(s2, b2 + p)
        return max(0, s1, s2)