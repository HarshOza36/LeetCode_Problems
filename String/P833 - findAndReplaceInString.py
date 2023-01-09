class Solution:
    def findReplaceString(self, S: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # starting in reverse, as per the rules, we will apply the operations
        # so we will sort the given data in reverse order of the indices
        
        data = sorted(zip(indices, sources, targets), reverse=True)
        for i, s, t in data:
            if S[i : i+len(s)] == s:
                S = S[:i] + t + S[i+len(s):]
        return S