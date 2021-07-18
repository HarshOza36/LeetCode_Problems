class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # A slow brute force approach
        temp = []
        for i in range(len(nums)):
            # temp = nums.copy() doesnt work in leetcode
            temp[:] = nums[:]
            del temp[i]
            if(all(temp[j] < temp[j+1] for j in range(len(temp)-1))):
                return True
                break
        return False

        # Better Solution
        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            if arr == sorted(arr) and len(arr) == len(set(arr)):
                return True
        return False
