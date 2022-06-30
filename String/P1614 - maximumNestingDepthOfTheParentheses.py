class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_depth = 0
        for ch in s:
            if(ch == "("):
                stack.append(ch)
            if(ch == ")"):
                stack.pop()
                max_depth = max(max_depth, len(stack) + 1)
            
        return max_depth