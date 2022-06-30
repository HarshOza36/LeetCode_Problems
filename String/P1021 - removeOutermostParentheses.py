class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = ""
        stack = []
        for ch in s:
            if(len(stack) == 0 ):
                stack.append(ch)
                continue
                
            if(ch == ')' and len(stack) == 1):
                stack.pop()
                continue
                
            if(ch == ')'):
                stack.pop()
                out += ch
                
            if(ch == '('):
                stack.append(ch)
                out += ch
        return out