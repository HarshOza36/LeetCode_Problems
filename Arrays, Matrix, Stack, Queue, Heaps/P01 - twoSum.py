class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force
        # i = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         try:
        #             if(nums[i] + nums[j] == target):
        #                 return [i,j]
        #         except:
        #             continue
        
        # Using Dictionary
        # comp = {}
        # for idx, num in enumerate(nums):
        #     c = target - num
        #     if c in comp:
        #         return [comp[c],idx]
        #     else:
        #         comp[num] = idx
        # return None     
    
        #Using Set
        hashset = set()
        for num_id,num in enumerate(nums):
            if(target - num in hashset):
                return (num_id,nums.index(target-num))
            else:
                hashset.add(num)
                
