class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a, b = sum(aliceSizes), sum(bobSizes)
        seen = set(bobSizes)
        # basically its two sum, where target is formed by the equation
        # sum of alice - a candy + bob candy = sum of bob - b candy + alice candy
        # bob candy = alice candy + (sum of bob candies - sum of alice candies)/2
        diff = (b-a)//2
        for C in aliceSizes:
            if C + diff in seen:
                return [C, C + diff]
        