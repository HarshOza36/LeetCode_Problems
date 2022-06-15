class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        # My method 
        # Xor start and goal, then count the number of ones in the binary in it
        xor = start ^ goal
        cnt = 0
        while(xor > 0):
            # xor & 1 will check if the last digit in binary rep is one
            # if its 1 , 1&1 will be 1 and will be added to cnt else 0
            cnt += xor & 1
            # right shifting my 1 and moving behind
            xor = xor >> 1
        return cnt