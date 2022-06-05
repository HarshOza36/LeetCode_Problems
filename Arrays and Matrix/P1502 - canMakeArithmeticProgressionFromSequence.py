class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        first_diff = abs(arr[1] - arr[0])
        for i in range(2, len(arr)):
            if(abs(arr[i] - arr[i-1]) != first_diff):
                return False
        return True