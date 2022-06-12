class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        l = 0
        currSum = 0
        max_sc = -1
        for r in range(len(nums)):
            add = nums[r]
            while(l < r and add in seen):
                seen.remove(nums[l])
                currSum -= nums[l]
                l += 1
            currSum += add
            seen.add(add)
            max_sc = max(max_sc, currSum)
        return max_sc
                
                