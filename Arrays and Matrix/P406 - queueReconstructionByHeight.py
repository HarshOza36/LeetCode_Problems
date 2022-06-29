class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Runs O(nlogn + n^2)
        people.sort(key = lambda x : (x[0],x[1]))
        # that is we will sort by first values and if first values are same we 
        # will sort by the second value in that case.
        
        n = len(people)
        ans = [[-1,-1] for _ in range(n)]
        for i in range(n):
            cnt = people[i][1]
            for j in range(n):
                # if output array has empty space and count reaches 0 we 
                # place the person.
                if cnt == 0 and ans[j][0] == -1:
                    ans[j] = people[i]
                    break
                # if there is an empty space or the current output person 
                # height is greater than the current person height we will 
                # skip that place move ahead
                elif(ans[j][0] == -1 or ans[j][0] >= people[i][0]):
                    cnt -= 1 # skip
        return ans
                    
                    