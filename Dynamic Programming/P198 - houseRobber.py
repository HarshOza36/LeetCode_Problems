class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can either take 0th value and next half, or start with next half
        # finally take its max
        # def helper(idx):
        #     if idx >= len(nums):
        #         return 0
        #     return max(nums[idx] + self.rob(nums[idx+2:]), self.rob(nums[idx+1:]))
        # return helper(0)
    
        # Iterative
        second_last_house, prev_house = 0, 0
        temp = 0
        for curr_house in nums:
            temp = max(curr_house + second_last_house, prev_house)
            second_last_house = prev_house
            prev_house = temp
        return prev_house