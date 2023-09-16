class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for fro, to in tickets:
            graph[fro].append(to)

        for k in graph.keys():
            graph[k].sort(reverse = True)
        

        itinerary = []
        def dfs(dest):
            while graph[dest]:
                nei = graph[dest].pop()

                if len(graph[nei]) == 0:
                    itinerary.append(nei)
                else:
                    dfs(nei)
            itinerary.append(dest)

        dfs('JFK')
        return itinerary[::-1]
            
            