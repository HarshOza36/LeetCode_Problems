class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        # Bruteforce
        # text = text.split()
        # count = len(text)
        # broken = set(brokenLetters)
        # for word in text:
        #     for w in word:
        #         if w in broken:
        #             count -= 1
        #             break
        # return count
    
        # HashSet Solution
        out = 0 
        brokenLetters = set(brokenLetters)
        for word in text.split(): 
            if(not set(word) & brokenLetters): 
                out += 1
        return out