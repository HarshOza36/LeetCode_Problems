class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) - 1
        if(s[0] == s[n]):
            return len(s) - 2
        
        seen = {}
        for idx,ch in enumerate(s):
            if(ch in seen):
                seen[ch].append(idx)
            else:
                seen[ch] = [idx]
                
        diff = -1
        
        for k,v in seen.items():
            if(len(v) > 1):
                diff = max(diff, v[len(v) - 1] - v[0] - 1)
                
        return diff
  