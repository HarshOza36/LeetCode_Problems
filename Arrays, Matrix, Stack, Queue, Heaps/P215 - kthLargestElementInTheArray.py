class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapify(heap)
        for n in nums:
            heappush(heap, -1 * n) # for max element
        ans = 0
        for i in range(k):
            ans = heappop(heap)
        return ans*-1