class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        seen, out = defaultdict(int), []
        for n in sorted(changed, reverse=True):
            if seen[n * 2]:
                seen[n * 2] -= 1
                out.append(n)
            else:
                seen[n] += 1
        
        # if all values are not zero 
        if any(seen.values()): return []
        return out