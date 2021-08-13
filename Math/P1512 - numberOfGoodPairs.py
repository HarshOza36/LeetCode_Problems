class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force
        # pairs = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if(nums[i] == nums[j] and i < j):
        #             pairs += 1
        # return pairs
        
        
        
#         [1,2,1,1,3,4,3] -> 4 pairs (3 pairs of 1 and 1 pair of 3)
#         Focus on [1,2,1,1] -> 3 pairs of 1. 
#         So when we reach 4th index our pair should be 3.
        pairs = 0
        d = {}
        for num in nums:
            if(num in d):
                pairs += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return pairs
        