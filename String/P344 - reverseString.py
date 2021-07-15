class Solution(object):
    def helper_reverse(self,s,left,right):
        if(left >= right):   
            return
        else:
            s[left],s[right] = s[right],s[left]
            self.helper_reverse(s,left+1,right-1)
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # easiest python approach
        # return s.reverse()
        # other approach is just loop using 2 pointers until left < right and swap all.
        # But we have to use recursion as they have asked for it
        return self.helper_reverse(s,0,len(s)-1)