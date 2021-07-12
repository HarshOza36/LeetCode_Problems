class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force that came up first
        # Removing Duplicates
        nums = list(set(nums))
        # if(len(nums) < 3):
        #     return max(nums)
        # elif(len(nums) == 3):
        #     return min(nums)
        # else:
        #     for i in range(2):
        #         nums.remove(max(nums))
        # return max(nums)
        
        # Using direct sorting
        # Sorting depends on the list, so runtime may be slow
        if(len(nums)<3):
            return max(nums)
        else:
            return sorted(nums,reverse=True)[2]
