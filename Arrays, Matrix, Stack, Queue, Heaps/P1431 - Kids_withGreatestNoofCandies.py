class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        # out_l = []
        # for i in candies:
        #     if(i + extraCandies >= max_candies):
        #         out_l.append(True)
        #     else:
        #         out_l.append(False)
        # return out_l
        
        # One Liner
        return [True if(i + extraCandies >= max_candies) else False for i in candies]