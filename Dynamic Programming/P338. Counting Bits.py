class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(n+1):
            binary_val = bin(i)
            arr.append(binary_val.count("1"))
        return arr