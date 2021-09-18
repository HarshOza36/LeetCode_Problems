class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1)
        
        freq = {}
        for ele in nums1:
            if(ele in freq):
                freq[ele] += 1
            else:
                freq[ele] = 1

        out = []
        for ele in nums2:
            if(ele in freq):
                if(freq[ele] > 0):
                    out.append(ele)
                    freq[ele] -= 1
        return out