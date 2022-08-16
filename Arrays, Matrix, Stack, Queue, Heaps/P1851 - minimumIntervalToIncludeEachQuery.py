class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # O(nlogn + qlogq)
        intervals.sort()
        ans = {}
        i = 0
        # creating minHeap
        heap = []
        
        for q in sorted(queries):
            
            # Adding intervals length and right element for tie
            # till the start of intervals <= query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            # popping all values, which do not belong to the query
            # for example, heap can have min value (1,3) but query is 5
            # through 3 we understand that , right was 3 for this interval
            # query 5 is greater than 3, hence this value is not proper
            # interval so we pop it.
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # Finally we append the min interval len
            # we made ans a dictionary because, the queries values we used
            # are sorted, but we need to return their exact index
            # so right now , we store its ans as value 
            ans[q] = heap[0][0] if heap else -1
            
        # now for original queries we will just add their value from ans
        
        return [ans[q] for q in queries]