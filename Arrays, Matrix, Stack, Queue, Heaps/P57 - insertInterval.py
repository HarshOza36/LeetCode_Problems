class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        ans = []
        for idx, (currStart, currEnd) in enumerate(intervals):
            newStart, newEnd = newInterval
            
            if newEnd < currStart:
                ans.append(newInterval)
                # if this newEnd was smaller than currStart
                # we know all intervals after this are not gonna overlap
                return ans + intervals[idx:]
            elif newStart > currEnd:
                # That means, the newInterval is still not added
                # may overlap head
                ans.append([currStart, currEnd])
            else:
                # Its overlapping, we can update the newInterval
                # It may overlap ahead so not adding to ans
                newInterval = [min(newStart, currStart), max(newEnd, currEnd)]        
        # If the first if never executes and we dont return
        # so we will add it now.
        ans.append(newInterval)
        return ans
                
                
                