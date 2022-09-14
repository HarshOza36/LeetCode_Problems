class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNeg = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                countNeg += 1
        return -1 if countNeg & 1 else 1