class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow,fast = 0,0
        while(slow < len(nums)):
            if(nums[slow]!=0 ):
                temp = nums[fast]
                nums[fast],nums[slow] = nums[slow],temp 
                slow += 1
                fast += 1
            else:
                slow += 1
            
  
