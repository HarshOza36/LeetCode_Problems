class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for i in range(len(colors)-1):
            if colors[i] == colors[i+1]:
                if neededTime[i] < neededTime[i+1]:
                    ans += neededTime[i]
                else:
                    ans += neededTime[i+1]
                    
                    # Now we move current ith value to i+1th
                    # because there might be consecutive colors ahead
                    
                    neededTime[i+1] = neededTime[i]
        return ans