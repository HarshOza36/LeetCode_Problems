class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for ele in arr:
            double = 2*ele
            half = ele//2
            if(double in seen or (ele%2 == 0 and half in seen)):
                return True
            else:
                seen.add(ele)
        return False
                
        
        