class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        i = j = 0

        while(i < len(firstList) and j < len(secondList)):
            fStart, fEnd = firstList[i][0], firstList[i][1]
            sStart, sEnd = secondList[j][0], secondList[j][1]
            # l,r are start, end of intersection respectively
            l = max(fStart, sStart)
            r = min(fEnd, sEnd)
            if l <= r:
                output.append([l, r])

            # checking if either interval is still on
            if(fEnd < sEnd):
                i += 1
            else:
                j += 1
        return output
