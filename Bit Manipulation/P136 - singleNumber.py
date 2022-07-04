class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bit manipulation O(n) time O(1) space
        ans = 0
        for n in nums:
            ans ^= n
        return ans
        
        # Found the below math solution in discussions but O(n) time and space
        # return 2*sum(set(nums))-sum(nums)
