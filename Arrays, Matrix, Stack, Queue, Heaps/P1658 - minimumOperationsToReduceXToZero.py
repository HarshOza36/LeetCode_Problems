class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # The number of elements removed =  n -  number of elements that aren't 
        # removed. Therefore, to find the minimum number of elements to remove, 
        # we can find the maximum number of elements to not remove!

        # So, instead of trying to find the minimum number of operations, why 
        # don't we focus on finding the longest subarray in the middle. One main 
        # thing to note is that our subarray should sum to sum - x (where sum is 
        # the sum of all elements in our array).
        longest_subarr_sum = sum(nums) - x
        l = 0
        n = len(nums)
        max_len = -1
        currSum = 0
        for r in range(n):
            currSum += nums[r]
            while(l <= r and currSum > longest_subarr_sum):
                currSum -= nums[l]
                l += 1
            if(currSum == longest_subarr_sum):
                max_len = max(max_len, r-l+1)
        return -1 if max_len == -1 else n - max_len