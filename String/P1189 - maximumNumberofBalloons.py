class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        freq = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for ch in text:
            if ch in freq:
                freq[ch] += 1
        
        # Finding minimum occurences required to form Balloon
        min_lo = min(freq['l'], freq['o']) // 2
        min_ban = min(freq['b'], freq['a'], freq['n'])
        
        return min(min_lo, min_ban)
        