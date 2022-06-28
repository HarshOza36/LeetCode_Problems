class Solution:
    def findStart(self, nums, target):
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) // 2
            if(nums[mid] == target and ((mid == 0) or nums[mid - 1] < target)):
                    return mid
            elif(nums[mid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1
                
#     def findEnd(self, nums, target):
#         l = 0
#         r = len(nums) - 1

#         while(l <= r):
#             mid = (l + r) // 2
#             if(((mid == len(nums) - 1) or (nums[mid + 1] > target)) and (nums[mid] == target)):
#                     return mid
#             elif(nums[mid] > target):
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # return [self.findStart(nums,target), self.findEnd(nums,target)]
        start = self.findStart(nums, target)
        if(start == -1):
            return [-1, -1]
        end = start

        for i in range(start, len(nums)):
            if(nums[i] == target):
                end = i
            else:
                break
        return [start, end]