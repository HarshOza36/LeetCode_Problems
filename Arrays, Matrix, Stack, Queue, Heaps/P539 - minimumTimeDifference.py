class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def convert(time):
		    hh, mm = time.split(':')
		    return int(hh) * 60 + int(mm)

        # one day has 24*60 = 1440 mins, so we can have 
        # fixed 1440 size table, and keep bool value if it is seen
        # or not
        time_slots = [False] * 1440
        start, end = 1440, -1
        for time in timePoints:
            mins = convert(time)
            if time_slots[mins]:
                # if we already got a same time then we have
                # min difference 0
                return 0

            time_slots[mins] = True
            start = min(start, mins)
            end = max(end, mins)
        # in start and end we will have our min and max mins
        # then we can loop through the seen minutes
        # and then find the minimum difference of time in that
        prev, res = start, start - end + 1440
        for curr in range(start + 1, end + 1):
            if not time_slots[curr]:
                continue
            res = min(res, curr - prev)
            prev = curr

        return res