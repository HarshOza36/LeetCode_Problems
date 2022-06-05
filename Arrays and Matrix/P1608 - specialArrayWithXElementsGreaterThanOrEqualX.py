class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) solution
        # for x in range(len(nums) + 1):
        #     cnt = 0
        #     for j in range(len(nums)):
        #         if(nums[j] >= x):
        #             cnt += 1
        #     if(cnt == x):
        #         return x
        # return -1
        
        # O(nlogn) solution
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        
        while(l <= r):
            mid = (l + r) // 2
            x = n - mid
            if(nums[mid] >= x):
                if(mid == 0 or nums[mid-1] < x):
                    return x
                else:
                    r = mid - 1
            else:
                l = mid + 1
        return -1
            