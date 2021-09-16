class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = a = b = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]: 
                a, b = 1, a + 1 
            elif arr[i] < arr[i - 1]: 
                a, b = b + 1, 1 
            else:
                a = b = 1 
            res = max(res, a, b) 
        return res
    
    