class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for n in range(left,right+1):
            num = str(n)
            if("0" not in num):
                flag = True
                for ch in num:
                    if(n%int(ch) != 0):
                        flag = False
                if(flag):
                    out.append(int(num))
        return out