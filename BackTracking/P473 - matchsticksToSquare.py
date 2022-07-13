class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # it is variation of 698 - Partition to K equal sum subsets with K = 4
        n = len(matchsticks)
        s = sum(matchsticks)
        side = s//4
        if s/4 != side:
            return False
        matchsticks.sort(reverse = True)
        # reversing will help us to check if any of the matches are too large to
        # fit in a side so we can immediately return false
        
        tlbr = [0]*4  # top left bottom right sides
        mem = set() # memoization
        def backtrack(idx):
            if idx == n:
                return True
            symbol = '.'.join(map(str, tlbr))
            if symbol in mem: return False
            mem.add(symbol)
            for j in range(4):
                if tlbr[j] + matchsticks[idx] <= side:
                    tlbr[j] += matchsticks[idx]
                    if backtrack(idx+1):
                        return True
                    tlbr[j] -= matchsticks[idx]
                    if tlbr[j] == 0: break # Game Changer
                    
            return False
        return backtrack(0)
    
    # Courtesy https://leetcode.com/Dwight_Kurt_Schrute
    # Game changer line makes the code super fast. Reduced my time from 3530ms to 227ms
    # The reason this works is that is the most important line in this code. 
    # It is saying that if you place a number (e.g. 4) as the "first item" into an 
    # empty bucket and all the backtracking fails, there's no need to try to 
    #  insert this 4 into another empty bucket. 
    # example:
    # let's say a = 6 and after a few iterations let tlbr = [5,4,0,0] after trying 
    # every possible way if tlbr[1] return 0 we can break it instead of moving it to 
    # the next empty bucket.
    # [5,4,0,0] is the same as [5,0,4,0] only the position of 4 changes but not the 
    # possible outcomes