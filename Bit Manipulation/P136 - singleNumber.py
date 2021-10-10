class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in nums:
        #     if(nums.count(i) == 1):
        #         return i
        # Above approach was superslow
        # By using XOR now
        single = 0
        for i in range(len(nums)):
            single = single^nums[i]
        return single
        
        # Found the below solution in discussions
        # return 2*sum(set(nums))-sum(nums)