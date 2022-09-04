class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        # Time O(m^2) Space O(n+m) where m = no of stops, n = no of bus routes
        if source == target:
            return 0
        
        # we will create a graph
        # where key is bus stops and values are the routes in which that stop exists
        
        graph = {}
        for route in range(len(routes)):
            for stop in routes[route]:
                if stop not in graph:
                    graph[stop] = set()
                
                graph[stop].add(route)
        
        
        visited_routes, visited_stops = set(), set()
        # queue will have (bus_stop_number, buses_taken)
        queue = deque([(source, 0)])
        
        # perform bfs
        while queue:
            stop, bus_taken = queue.popleft()
            visited_stops.add(stop)
            if stop == target:
                return bus_taken
            
            # Now we will add, all the next stops we can reach by changing or staying in the bus
            for new_route in graph[stop]:
                if new_route not in visited_routes:
                    for new_stop in routes[new_route]:
                        if new_stop not in visited_stops:
                            queue.append((new_stop, bus_taken + 1))
                    # now adding the bus route that we took since we added all 
                    # its routes
                    visited_routes.add(new_route)
        return -1
            