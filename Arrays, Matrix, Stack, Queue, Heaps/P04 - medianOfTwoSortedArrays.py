class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1+nums2)
        if(len(nums) == 1):
            return float(nums[0])
        elif(len(nums) % 2 == 0):
            return (float(nums[len(nums)//2 - 1] + nums[len(nums)//2])/2)
        else:
            return float(nums[len(nums)//2])
