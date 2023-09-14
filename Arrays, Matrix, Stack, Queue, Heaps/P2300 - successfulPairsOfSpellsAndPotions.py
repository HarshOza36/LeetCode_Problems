class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def search(currSpell):
            n = len(potions)
            l = 0
            r = n - 1
            while l <= r:
                mid = (l+r) // 2
                prod = potions[mid] * currSpell
                if prod >= success:
                    r = mid - 1
                elif prod < success:
                    l = mid + 1
            return n - l

        ans = []
        for spell in spells:
            ans.append(search(spell))
        return ans