class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # this problem is quite similar to non overlapping intervals
        # because we just need to find the non overlapping diameters

        # we will sort as per the end points
        # then we will keep updating the end points whenever the starts are 
        # greater than the previous ends, so that we can shoot minimum arrows
        # as per the number of non overlapping intervals we have

        points.sort(key = lambda x : x[1])
        ans = 1
        prevEnd = points[0][1]
        for currStart, currEnd in points[1:]:
            if currStart > prevEnd:
                prevEnd = currEnd
                ans += 1  
        return ans