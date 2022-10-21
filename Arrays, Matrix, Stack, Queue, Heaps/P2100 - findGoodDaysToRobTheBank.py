class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        
        nonIncreasing = [0]*n # no of days values decrease
        nonDecreasing = [0]*n # no of days values increase
        
        for i in range(1, n):    
            # nonIncreasing
            if security[i-1] >= security[i]:
                nonIncreasing[i] = nonIncreasing[i-1] + 1
                
            # NonDecreasing check from reverse end
            if security[-i] >= security[-i-1]:
                nonDecreasing[-i-1] = nonDecreasing[-i] + 1
                
        ans = []
        for i in range(n):
            # now wherever, we find values of nonincreasing and nondecreasing
            # are >= time give those will be the good days
            if nonIncreasing[i] >= time and nonDecreasing[i] >= time:
                ans.append(i)
        return ans