class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prevEnd = intervals[0][1]
        for currStart, currEnd in intervals[1:]:
            if currStart >= prevEnd:
                # Not overlapping
                prevEnd = currEnd
            else:
                # Overlap found
                ans += 1
                # we will want to keep the interval which ends first in 
                # overlap , so that next starts have less chances of 
                # overlap
                prevEnd = min(prevEnd, currEnd)
        return ans