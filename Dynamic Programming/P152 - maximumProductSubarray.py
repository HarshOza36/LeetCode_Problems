class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax, currMin = 1, 1
        
        # we keep track of min and max
        # because if we have negatives, is it possible
        # that further a number is again negative
        # and when we multiple the subarray we will get a positive max
        # subarray
        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = currMax * n # since we are changing it and will be needed ahead
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp, n*currMin, n)
            res = max(res, currMax, currMin)
        return res