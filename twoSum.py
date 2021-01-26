class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                try:
                    if(nums[i] + nums[j] == target):
                        return [i,j]
                except:
                    continue
