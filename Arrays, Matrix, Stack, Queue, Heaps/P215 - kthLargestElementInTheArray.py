class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # O(nlogn)
        # nums.sort()
        # return nums[len(nums) - k]
        
        # O(n + klogn)
#         heap = [-n for n in nums] # runs o(n)
#         heapify(heap) # runs o(n)
        
#         ans = 0
#         # Runs O(k)
#         for i in range(k):
#             ans = heappop(heap) # O(logn)
#         return -ans
        
        # QuickSelect O(n) avg O(n^2) worst
        
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, ptr = nums[r], l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            
            nums[ptr], nums[r] = nums[r], nums[ptr]
            
            if k < ptr:
                return quickSelect(l, ptr - 1)
            elif k > ptr:
                return quickSelect(ptr + 1, r)
            else:
                return nums[ptr]
        
        return quickSelect(0, len(nums) - 1)