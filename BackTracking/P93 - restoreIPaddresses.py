class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12: return
        ans = []
        def backtrack(idx, section, curr):
            if section == 4 and idx == n:
                ans.append(curr[:-1])
                return
            if section > 4: return
            # we will loop for next 3 indices and check if they are valid
            for i in range(idx, min(idx+3, n)):
                if int(s[idx: i+1]) < 256 and (idx == i or s[idx] != '0'):
                    backtrack(i + 1, section + 1, curr + s[idx:i+1] + '.')
        backtrack(0, 0, "")
        return ans