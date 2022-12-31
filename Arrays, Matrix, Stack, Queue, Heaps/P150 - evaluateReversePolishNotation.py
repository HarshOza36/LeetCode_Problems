class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        oprs = {
            '+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul
        }
        stack = []
        for ch in tokens:
            if ch in oprs:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                op = oprs.get(ch)
                stack.append(int(op(op1, op2)))
            else:
                stack.append(ch)
        return stack[-1]