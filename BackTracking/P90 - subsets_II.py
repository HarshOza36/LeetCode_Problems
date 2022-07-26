class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        out = []
        nums.sort()
        
        def helper(idx, subset):
            if idx >= len(nums):
                out.append(subset[::])
                return
            
            # Including element
            subset.append(nums[idx])
            helper(idx+1, subset)
            
            # Excluding element
            subset.pop()
            # Say the element we are excluding above is 2
            # since nums is sorted, we skip duplicates since we dont want 
            # any of these 2 ahead
            
            while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            
            # Only after excluding, we will go ahead.
            helper(idx+1, subset)
            
        helper(0, [])
        return out