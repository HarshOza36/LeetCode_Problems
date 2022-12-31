class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # we will sort the tasks by enqueue time, if same, then processing time
        # if both are same then by index, we will sort in descending order
        # so when we want to take the task we can use pop() from the list
        # to get the tasks.
        tasks = sorted([(enqTime, procTime, idx)
                        for idx, (enqTime, procTime) in enumerate(tasks)], reverse=True)
        
        ans = []
        currTime = 0
        pq = []

        while tasks or pq:
            if not pq:
                # if queue is empty, then move to the next enqueue time
                currTime = max(currTime, tasks[-1][0])
            
            while tasks and tasks[-1][0] <= currTime:
                # adding all the tasks arriving by current time
                enqTime, procTime, idx = tasks.pop()
                heappush(pq, (procTime, idx))
            
            # Now processing the tasks and adding it to the current time
            nextProc, nextIdx = heappop(pq)
            ans.append(nextIdx)
            currTime += nextProc
        return ans
