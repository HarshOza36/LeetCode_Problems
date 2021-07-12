class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Simple brute force
        # while val in nums:
        #     nums.remove(val)
        # return (len(nums))
    
        # Trying a 2 pointer approach which should be faster
        k = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k+=1
        return k