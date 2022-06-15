class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_ch = 0
            # Constructing allowed characters as a binary
            # for example we have abz then
            # bits 25, 1, 0 will be set in the binary literal
            # so everytime we will calculate ch - 'a' and Left shift it by 1
            # say we have c - a, which is 2, we will do 1<<2 to get 0100, 
            # OR it will allowed_ch to get whatever was there before and add this to it
            # say allowed_ch was 0001 that is a is allowed and 0001 | 0100 = 0101 that means c and a are allowed
            
        for ch in allowed:
            allowed_ch |= 1 << (ord(ch) - 97)
        
        # Now we will just AND each characters value left shifted by one
        # If we get all 0 then that character wont be there in the allowed list.
        cnt = 0
        for word in words:
            for ch in word:
                flag = True
                if(allowed_ch & (1 << (ord(ch) - 97)) == 0):
                    flag = False
                    break
            if(flag):
                cnt += 1
        return cnt
            