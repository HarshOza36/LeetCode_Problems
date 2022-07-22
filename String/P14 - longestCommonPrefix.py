class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Runs O(max(len(inner str)) * len(strs))
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    # if len(s) is out of bound or our characters dont match
                    return res
            res += strs[0][i]
        return res
                