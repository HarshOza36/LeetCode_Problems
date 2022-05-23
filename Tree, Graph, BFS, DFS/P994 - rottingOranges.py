class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited, curr = set(), deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    visited.add((i, j))
                elif(grid[i][j] == 2):
                    curr.append((i, j))
        count = 0
        while visited and curr:
            for c in range(len(curr)):
                i, j = curr.popleft()
                for x,y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if (x,y) in visited:
                        visited.remove((x,y))
                        curr.append((x,y))
            count += 1
		
        # If there are still fresh oranges we return -1 else the count
        return -1 if visited else count