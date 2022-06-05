class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Bruteforce Time Limit Exceeded - O(n^2)
        # l = 0
        # r = 1
        # min_found = float('inf')
        # while(r <= len(nums) and l <= r): 
        #     temp_arr = nums[l:r]
        #     sum_arr = sum(temp_arr)
        #     if(sum_arr >= target):
        #         min_found = min(min_found, len(temp_arr))
        #         l += 1
        #         r = l + 1
        #     else:
        #         r += 1
        # return 0 if min_found == float('inf') else min_found
        
        # O(n) approach
        l = 0
        min_found, subarray_sum = float('inf'), 0

        for r in range(len(nums)):
            subarray_sum += nums[r]
            while subarray_sum >= target:
                min_found = min(min_found, r - l + 1)
                subarray_sum -= nums[l]
                l += 1
        return 0 if min_found == float('inf') else min_found