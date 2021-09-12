class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        num = 0
        sign = 1
        res = 0
        stack = []
        op = ["+","-"]
        for ele in s:
            if ele.isdigit():
                num = 10*num + int(ele)
            elif ele in op:
                res += sign*num
                num = 0
                sign = 1 if(ele == "+") else -1
            elif ele == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ele == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign