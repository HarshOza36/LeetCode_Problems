class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # This problem is same as Leetcode 1011, with weights as nums, and days as k
        
        weights = nums
        days = k
        
        def findLeastCap(targetCap):
            currDay = 1
            items = 0
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