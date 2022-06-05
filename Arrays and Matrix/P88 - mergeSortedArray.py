class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        n1 = m - 1
        n2 = n - 1
        main = len(nums1) - 1
        while(n1 >= 0 and n2 >= 0):
            if(nums1[n1] < nums2[n2]):
                nums1[main] = nums2[n2]
                n2 -= 1
            else:
                nums1[main] = nums1[n1]
                n1 -= 1
            main -= 1

        for i in range(n2, -1, -1):
            nums1[main] = nums2[i]
            main -= 1