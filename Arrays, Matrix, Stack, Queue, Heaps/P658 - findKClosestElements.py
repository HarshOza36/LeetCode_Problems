class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Bruteforce O(n +klogk)
        heap = []
        # O(n)
        for val in arr:
            heap.append((abs(x-val), val))
            
        # O(n)
        heapify(heap)

        
        # O(klogk)
        ans = [heappop(heap)[1] for i in range(k)]
        ans.sort()
        return ans
        

        