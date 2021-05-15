class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0 
        while (c < len(nums)-1):
            if(nums[c] == nums[c+1]):
                del nums[c]
            else:
                c += 1
        return len(nums)
                