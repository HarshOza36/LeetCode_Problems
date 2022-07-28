class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#         out = set()
#         if len(nums) < 3:
#             return out

#         nums.sort()
#         for i in range(len(nums)):
#             target = -nums[i]
#             temp = dict()
#             for j in range(i+1,len(nums)): 
#                 if(target - nums[j] in temp):
#                     out.add((nums[i],nums[j],nums[temp[target - nums[j]]]))
#                 else:
#                     temp[nums[j]] = j
#         return [list(i) for i in out]

    # brute force above had repetitions below is more optimized code
    if len(nums) < 3:
            return []
        res = []
        nums.sort()
        
        for i, first in enumerate(nums):
            if i > 0 and first == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while(l < r):
                threeSum = first + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([first, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
        
    
