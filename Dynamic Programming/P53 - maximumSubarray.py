class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)