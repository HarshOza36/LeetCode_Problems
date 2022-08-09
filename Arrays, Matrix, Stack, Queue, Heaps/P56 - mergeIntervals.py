class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        for start, end in intervals:
            if not ans or ans[-1][1] < start:
                ans.append([start, end])
            else:
                # if prev end is >= start, then we just change
                # prev intervals end to new end
                # we will take max because say [[1,4],[2,3]]
                # here we cannot just replace 4 with 3
                # it has to be their max
                ans[-1][1] = max(ans[-1][1], end)
        return ans
            