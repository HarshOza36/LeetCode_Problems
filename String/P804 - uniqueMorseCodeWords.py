class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
                      ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
                      "...","-","..-","...-",".--","-..-","-.--","--.."]
        
        seen = set()
        for w in words:
            morse = ""
            for ch in w:
                morse += morseCodes[ord(ch) - ord('a')]
            seen.add(morse) 
        return len(seen)