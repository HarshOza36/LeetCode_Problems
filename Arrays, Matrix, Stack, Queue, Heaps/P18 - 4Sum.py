class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twoSum(nums, target):
            res = []
            s = set()
            for num in nums:
                if len(res) == 0 or res[-1][1] != num:
                    complement = target - num
                    if complement in s:
                        res.append([complement, num])
                s.add(num)
            return res

        def kSum(nums, target, k):
            res = []
            if not nums: return res
            
            # There are k remaining values to add to the sum. 
            # The average of these values is at least target // k.
            average_value = target // k
            
            # We cannot obtain a sum of target if the smallest value
            # in nums is greater than average_value or if the largest 
            # value in nums is smaller than average_value.
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            
            if k == 2:
                return twoSum(nums, target)
    
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    nextSum = kSum(nums[i + 1:], target - nums[i], k - 1)
                    for subset in nextSum:
                        res.append([nums[i]] + subset)
            return res

        

        nums.sort()
        return kSum(nums, target, 4)