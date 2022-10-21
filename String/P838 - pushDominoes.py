class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        # so we will calculate the distance by pushing the R and L dominoes one 
        # by one, which will give us how far they can fall till interrupted
        # then we will subtract right-left distance, if we still have positive 
        # distance, dominoes are falling Right, if neg then left else 0
        
        left = [0] * len(dominoes)
        right = [0] * len(dominoes)
        
        rightDistance = 0
        for i in range(len(dominoes)):
            if dominoes[i] == "R":
                rightDistance = len(dominoes)
            
            elif dominoes[i] == ".":
                rightDistance = max(rightDistance-1, 0)
            else:
                rightDistance = 0 # if we hit L
            
            right[i] += rightDistance
        
        
        leftDistance = 0
        for i in range(len(dominoes)-1,-1,-1):
            if dominoes[i] == "L":
                leftDistance = len(dominoes)
            
            elif dominoes[i] == ".":
                leftDistance = max(leftDistance-1, 0)
            else:
                leftDistance = 0 # if we hit R
            
            left[i] += leftDistance
        
        ans = ""
        for i in range(len(dominoes)):
            distanceVal = right[i] - left[i]
            if distanceVal > 0:
                ans += "R"
            elif distanceVal < 0:
                ans += "L"
            else:
                ans += "."
        return ans
            