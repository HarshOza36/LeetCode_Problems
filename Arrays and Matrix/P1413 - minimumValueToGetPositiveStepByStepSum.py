class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = min_sum = 0
        for n in nums:   
            sum += n
            min_sum = min(min_sum, sum)
    
        return  -1 * min_sum + 1