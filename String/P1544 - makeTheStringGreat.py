class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        stack = []
        for ch in s:
            if stack and (stack[-1].upper() == ch or ch.upper() == stack[-1]) and ch != stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)