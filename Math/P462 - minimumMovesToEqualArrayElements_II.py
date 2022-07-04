class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sorting the array and incrementing decrementing elements as per the 
        # middle element i.e. median
        n = len(nums)
        if(n == 1):
            return 0
        nums.sort()
        mid = nums[n // 2]
        cnt = 0
        for n in nums:
            cnt += abs(mid - n)
        return cnt