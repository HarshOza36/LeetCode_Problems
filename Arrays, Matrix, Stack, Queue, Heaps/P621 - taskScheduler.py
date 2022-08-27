class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        
        # we will start with most frequent task first.
        # saving freq max O(26) since A-Z
        
        freq = {}
        for ch in tasks:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
        # we will save freq of character in the heap
        # heap will have max 26 element of A-Z hence O(26)
        heap = [-f for ch, f in freq.items()]
        heapq.heapify(heap)
        
        # all heap operations are O(logn) but here we just have max 26
        # so they will be O(26)
        
        q = deque()
        time = 0
        
        while heap or q:
            time += 1
            if heap:
                f = heapq.heappop(heap)
        
                f += 1 # since it is complete now we will deduct one
                # notice we add -freq because we want max heap so we ++ here
        
                if f:
                    # freq, next add time
                    q.append([f, time + n])
            
            # If the process can be rescheduled, add it to heap
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time
            