class Solution:
    def canAttendMeetings(self, intervals):
        # Note: (0,8) and (8,10) is not a conflict
        intervals.sort()
        prevEnd = intervals[0][1]
        for currStart, currEnd in intervals[1:]:
            if currStart < prevEnd:
                return False
            prevEnd = currEnd
        return True
