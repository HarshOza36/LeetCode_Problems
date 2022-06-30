class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # As asked for stack using O(m+n) time and space
        # stack1 = []
        # stack2 = []
        # for ch in s:
        #     if(ch == "#"):
        #         if(len(stack1) > 0): stack1.pop()
        #     else:
        #         stack1.append(ch)
        # for ch in t:
        #     if(ch == "#"):
        #         if(len(stack2) > 0): stack2.pop()
        #     else:
        #         stack2.append(ch)
        # return stack1 == stack2
        
        # Now with O(1) space
        l = len(s) - 1
        r = len(t) - 1
        s_skips = t_skips = 0
        while(l >= 0 or r >= 0):
            while(l >= 0):
                if(s[l] == "#"):
                    s_skips += 1
                    l -= 1
                elif(s_skips > 0):
                    l -= 1
                    s_skips -= 1
                else:
                    break
            while(r >= 0):
                if(t[r] == "#"):
                    t_skips += 1
                    r -= 1
                elif(t_skips > 0):
                    r -= 1
                    t_skips -= 1
                else:
                    break
            if(l >= 0 and r >= 0 and s[l] != t[r]):
                # when we have characters left we have to check the elements have to be same, if we have ac and ab, c and b dont match so return false
                return False
            if((l >= 0) != (r >= 0)): 
                # if the lengths become different there will be no way to get same string result
                return False
            l -= 1
            r -= 1
        return True