class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        if len(nums) < 3:
            return out

        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            temp = dict()
            for j in range(i+1,len(nums)): 
                if(target - nums[j] in temp):
                    out.add((nums[i],nums[j],nums[temp[target - nums[j]]]))
                else:
                    temp[nums[j]] = j
        return [list(i) for i in out]