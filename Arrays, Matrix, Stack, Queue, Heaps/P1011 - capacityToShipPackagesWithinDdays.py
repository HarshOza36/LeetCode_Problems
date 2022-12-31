class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # to get the capacity, the minimum capacity ship has to have will the maximum weight 
        # that we will have while the maximum capacity, we can have is the sum of all weights.

        # now we have to find the least possible weight capacity of the ship
        # we can binary search in the range of minCap - min(weights) and maxCap - sum(weights)

        # Every time when we find mid, we will then check, if we can allocate all the packages
        # in given days with that ship capacity


        # Time complexity - O(wlogn) where n = maxCap - minCap and w = len(weights)

        def findLeastCap(targetCap):
            currDay = 1
            items = 0
            # we traverse through weights
            # keep adding the items on a given day, until we reach
            # targetCap and if we can allocate everything we return 
            # true else False
            for w in weights:
                items += w
                if items > targetCap:
                    currDay += 1
                    if currDay > days: return False
                    items = w
            return True


        l, r = float("-inf"), 0
        for w in weights:
            l = max(l, w)
            r += w

        while l <= r:
            mid = (l+r) // 2
            if findLeastCap(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l