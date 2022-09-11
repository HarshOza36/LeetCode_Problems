class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        
        nums.sort()
        result = float(inf)
        
        for i in range(len(nums)-2):
            # ignore the duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum == target:
                    return target
                
                # compare the current and previous difference
                # if current is smaller i.e. closest, result = curSum
                if abs(curSum - target) < abs(result - target):
                    result = curSum
                    
                if curSum <= target:
                    l += 1
                    # ignore the further duplicate numbers
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r -= 1   
        return result