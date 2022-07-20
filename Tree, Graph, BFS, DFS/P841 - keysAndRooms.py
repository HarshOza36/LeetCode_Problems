class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            visited.add(node)
            for n in rooms[node]:
                if n not in visited:
                    stack.append(n)
        return True if len(visited) == len(rooms) else False