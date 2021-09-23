class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def findMaxSubsetLength(s,ind,n):
            if(ind >= n):
                self.ans = max(self.ans,len(s))
                return 
            findMaxSubsetLength(s,ind+1,n)
            new_s = s + arr[ind]
            if(len(new_s) == len(set(new_s))): # checking if there are no duplicates
                findMaxSubsetLength(new_s,ind+1,n)
        
        self.ans = 0
        findMaxSubsetLength("",0,len(arr))
        return self.ans