class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        # finding the first occurence wher number is greater which will be at i-1
        while i and nums[i-1] >= nums[i]: 
            i -= 1
        
        j = n - 1
        # finding the next smaller number than i
        while j > i and i and nums[j] <= nums[i-1]:
            j -= 1
        
        # swapping these numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # reversing the half from the first greater number
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1