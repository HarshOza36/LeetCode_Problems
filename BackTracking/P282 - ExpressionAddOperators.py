class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []
        def recurse(i, s, leading):
            if i > n-1:
                if eval(s) == target:
                    ans.append(s)
                return
            
            if leading != '0':
                recurse(i+1, s+num[i], leading)
            recurse(i+1, s+"+"+num[i], num[i])
            recurse(i+1, s+"-"+num[i], num[i])
            recurse(i+1, s+"*"+num[i], num[i])
            
        recurse(1, num[0], num[0])
        
        return ans
    
#       Instead of direct eval we can create our evaluate function
#         def evaluate(s):
#             a = []
#             temp = ""
#             for c in s:
#                 if '0' <= c <= '9': 
#                     temp += c
#                 else:
#                     a.append(int(temp))
#                     a.append(c)
#                     temp = ""
#             a.append(int(temp))
            
#             total = a[0]
#             prev = a[0]
#             for i in range(len(a)-1):
#                 item = a[i]
#                 if item == '+':
#                     total = total + a[i+1]
#                     prev = a[i+1]
#                 elif item == '-':
#                     total = total - a[i+1]
#                     prev = -a[i+1]
#                 elif item == '*':
#                     total = total - prev + prev * a[i+1]
#                     prev = prev * a[i+1]
#             return total