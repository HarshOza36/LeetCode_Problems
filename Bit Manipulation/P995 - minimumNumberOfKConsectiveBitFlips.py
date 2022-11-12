class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        totalFlips = 0
        currentValidFlips = 0 # it will tell valid flip for current index
        
        # we need a lookup table so that we can check
        # if i-k was ever flipped, that means,
        # the element which was just out of current window
        # then we will decrease the currentValidFlips
        # basically this is a left pointer in sliding windows
        # from which we will manage the repeat flips and it will be out
        # of the current valid sliding window range     
        isFlipped = [False] * n
        
        

        for i,num in enumerate(nums):
            if i >= k:
                # that means, some numbers are already seen and 
                # not in current window
                if isFlipped[i-k]:
                    currentValidFlips -= 1
                    
            if currentValidFlips % 2 == num:
                # if 0 == 0: this means not flipped
                # if 1 == 1: odd count, has to be flipped again
                if i + k > n: # we cannot get all 1
                    return -1
                
                currentValidFlips += 1
                isFlipped[i] = True
                totalFlips += 1
        return totalFlips