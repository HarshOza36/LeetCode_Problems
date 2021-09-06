class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits == ""):
            return []
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        if(len(digits) == 1):
            return list(d[digits])
        else:
            ans = list(d[digits[0]])
            for i in range(1,len(digits)):
                temp = []
                for j in range(len(ans)):
                    for ch in list(d[digits[i]]):
                        temp.append(ans[j]+ch)
                ans = temp
        return ans
                    