class Solution:
    def minMeetingRooms(self, intervals):
        # This problem can be brought down to
        # Finding the maximum number of overlapping intervals(meetings)
        # at any given time.
        
        startTimes = sorted([i[0] for i in intervals])
        EndTimes = sorted([i[1] for i in intervals])
        l, r = 0, 0
        meetingsGoingOn = 0
        res = 0
        # We will maintain a count which is meetingsGoingOn
        # every time, we will take min of l and r for each start and end
        # if min is start meetings += 1 and shift l else decrement and shift r
        # if there is a tie. then we will visit end time, move r and decrement
        while l < len(startTimes) and r < len(endTimes):
            if startTimes[l] < endTimes[r]:
                meetingsGoingOn += 1
                l += 1
            else:
                meetingsGoingOn -= 1
                r += 1
            res = max(res, meetingsGoingOn)
        return res
                
            
        
