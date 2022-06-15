class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        while num > 0:
            # Check if number is even
            if((num & 1) == 0):
                # Dividing number by 2
                num = num >> 1
            else:
                # Subtracting 1 from it
                num = num & (~1)
            cnt += 1
        return cnt