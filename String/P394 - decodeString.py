class Solution:
    def decodeString(self, s: str) -> str:
        # Brute force very slow because of multiple slicing and .joins each O(len string inside [])
#         stack = []
#         for ch in s:
#             if ch == ']':
#                 temp_str = []
#                 while stack[-1] != '[':
#                     temp_str.append(stack.pop())
#                 temp_str = "".join(temp_str[::-1])
#                 # now popping the '['
#                 stack.pop()
#                 # now multiplying the str and inserting back to stack
#                 stack.append(temp_str * stack.pop())
            
#             # combining numbers if they are more than one digit
#             elif(48 <= ord(ch) <= 57):
#                 if(stack and isinstance(stack[-1], int)):
#                     stack[-1] = 10*stack[-1] + int(ch)
#                 else:
#                     stack.append(int(ch))
#             else:
#                 stack.append(ch)
#         return "".join(stack)
        stack = []
        multiplier = 0 
        currString = ""
        for ch in s:
            if ch == '[':
                stack.append(currString)
                stack.append(multiplier)
                currString = ''
                multiplier = 0
            elif ch == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num*currString
            elif ch.isdigit():
                multiplier = multiplier*10 + int(ch)
            else:
                currString += ch
        return currString