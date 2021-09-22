class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp_max, ans = 0, 0
        for i in nums:
            if i == 1:
                temp_max += 1
                ans = max(ans, temp_max)
            else:
                temp_max = 0    
        return ans
        