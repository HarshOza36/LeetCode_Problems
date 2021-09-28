class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l, r, n = 0, 1, len(nums)
        while(l < n and r < n):
            if(nums[l] % 2 == 0):
                l += 2
            elif(nums[r] % 2 == 1):
                r += 2
            else:
                nums[l], nums[r] = nums[r], nums[l]
        return nums
                
            