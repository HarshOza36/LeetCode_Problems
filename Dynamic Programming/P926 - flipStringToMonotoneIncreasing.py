class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        # we split the string into left part and right part, and count how many ones in left and zeros in right
        left_ones = 0 
        right_zeroes = s.count("0")
        ans = right_zeroes
        for c in s:
            if c == "1": left_ones += 1
            if c == "0": right_zeroes -= 1
            ans = min(ans, right_zeroes + left_ones)
        return ans