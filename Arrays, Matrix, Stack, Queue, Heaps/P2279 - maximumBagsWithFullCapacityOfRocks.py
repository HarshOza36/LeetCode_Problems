class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bagRocks = sorted(zip(capacity, rocks), key = lambda x: x[0] - x[1])
        
        full = 0
        for cap, rock in bagRocks:
            if cap == rock:
                full += 1
                continue

            rem = cap - rock
            if additionalRocks - rem >= 0:
                additionalRocks -= rem
                full += 1

        return full