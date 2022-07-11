class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Pythonic
        # return nums*2
        result = [0] * (len(nums) * 2)
        for i in range(len(nums)):
            result[i], result[len(nums) + i] = nums[i], nums[i] 
        return result
        