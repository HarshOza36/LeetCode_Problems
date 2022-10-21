class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for box, units in boxTypes:

            ans += min(box, truckSize) * units
            truckSize -= box
            if truckSize <= 0:
                return ans
        return ans