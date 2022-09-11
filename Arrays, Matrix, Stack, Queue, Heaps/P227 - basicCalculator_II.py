class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        stack = []
        operation = "+"
        # at start any number we get, we just want to add it in stack
        # and we will keep track of all prev operation using this
        
        currNum = 0
        ops = {"+", "-", "*", "/"}
        for idx, ch in enumerate(s):
            if ch.isdigit():
                currNum = currNum*10 + int(ch)
                
            if ch in ops or idx == len(s) - 1:
                if operation == "-":
                    stack.append(-currNum)
                elif operation == "+":
                    stack.append(currNum)
                elif operation == "*":
                    stack.append(stack.pop() * currNum)
                elif operation == "/":
                    num = stack.pop()
                    # random python issue -3//2 is 2 since its floor
                    if num < 0:
                        val = -((-num) // currNum)
                    else:
                        val = num // currNum
                    stack.append(val)
                operation = ch
                currNum = 0
        ans = 0
        while stack:
            ans += stack.pop()
        return ans