class Solution:
    def __init__(self,):
        self.out = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, ans):
            if(len(nums) == 0):
                self.out.append(ans)
                return
            
            for idx, ele in enumerate(nums):
                curr = ele
                remaining = nums[:idx] + nums[idx+1:]
                helper(remaining, ans + [curr])
        helper(nums, []) 
        return self.out