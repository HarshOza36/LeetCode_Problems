class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occur = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        out = []
        for i, ch in enumerate(s):
            end = max(end, last_occur[ch])
            if i == end:
                out.append(i - start + 1)
                start = i + 1
            
        return out