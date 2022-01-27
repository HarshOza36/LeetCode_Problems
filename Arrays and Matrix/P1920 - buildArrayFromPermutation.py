class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for i in range(len(nums)):
        #     ans.append(nums[nums[i]])
        # return ans
        
        # O(1) space
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + (nums[nums[i]] % n) * n
        for i in range(n):
            nums[i] = nums[i] // n
        return nums