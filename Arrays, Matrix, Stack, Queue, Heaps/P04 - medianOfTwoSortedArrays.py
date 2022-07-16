class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Brute force
#         nums = sorted(nums1+nums2)
#         if(len(nums) == 1):
#             return float(nums[0])
#         elif(len(nums) % 2 == 0):
#             return (float(nums[len(nums)//2 - 1] + nums[len(nums)//2])/2)
#         else:
#             return float(nums[len(nums)//2])
        # O(log(min(n,m))
        m, n = len(n1), len(n2)
        total = m+n
        half = total//2
        
        # we want binary search on smaller array and want  it to be n2
        if m < n:
            m, n = n, m
            n1, n2 = n2, n1
            
        l,r = 0, n-1
        while True:
            n2_mid = (l + r) // 2
            # using mid at n2, we set mid of n1 with half, so that partitions are proper.
            n1_mid = half - n2_mid -1 -1
            
            n1_L = n1[n1_mid] if n1_mid >= 0 else float('-inf')
            n1_R = n1[n1_mid + 1] if n1_mid < m-1 else float('inf')
            n2_L = n2[n2_mid] if n2_mid >= 0 else float('-inf')
            n2_R = n2[n2_mid + 1] if n2_mid < n-1 else float('inf')

            # check if partition formed is correct
            if n1_R >= n2_L and n1_L <= n2_R:
                if total % 2 == 1:
                    return min(n1_R, n2_R)
                else:
                    return (max(n1_L, n2_L) + min(n1_R, n2_R)) / 2
            elif(n1_R < n2_L):
                r = n2_mid - 1
            else:
                l = n2_mid + 1
        
