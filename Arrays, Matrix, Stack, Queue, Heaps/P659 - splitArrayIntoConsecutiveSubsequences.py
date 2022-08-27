class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        # stores number frequency
        freqMap = defaultdict(int)
        # stores the next number in already filled subsequence
        nextMap = defaultdict(int)
        
        for n in nums: freqMap[n] += 1
            
        for n in nums:
            # if number is not in freq or has lost all its occurence 
            if not freqMap[n]: continue
                
            if nextMap[n]:
                # if we already have the number
                # we reduce its occurence and add next number in the map
                nextMap[n] -= 1
                nextMap[n+1] += 1
            # Otherwise we create the new subsequence by checking next and next to next values
            elif freqMap[n+1] and freqMap[n+2]:
                # decrease occurences
                freqMap[n+1] -= 1
                freqMap[n+2] -= 1
                # add n+2's next that is n+3
                nextMap[n+3] += 1
                
            else:
                # if they do not exist we will return false
                return False
            
            freqMap[n] -= 1
			
        return True