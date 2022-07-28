class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # it is combination sum with Subsets II
        out = []
        candidates.sort()
        
        def helper(idx, subset, total):
            if total == target:
                out.append(subset[::])
                return
            if idx >= len(candidates) or total > target:
                return
            
            # Including element
            subset.append(candidates[idx])
            helper(idx+1, subset, total + candidates[idx])
            
            # Excluding element
            subset.pop()
            # Say the element we are excluding above is 2
            # since nums is sorted, we skip duplicates since we dont want 
            # any of these 2 ahead
            
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            
            # Only after excluding, we will go ahead.
            helper(idx + 1, subset, total)
            
        helper(0, [], 0)
        return out
