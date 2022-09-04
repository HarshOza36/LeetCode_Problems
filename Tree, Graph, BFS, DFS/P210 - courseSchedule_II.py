class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for courses, preReq in prerequisites:
            adjList[courses].append(preReq)
        ans, visited, cycle = [], set(), set()
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for preReq in adjList[course]:
                if not dfs(preReq):
                    return False
            cycle.remove(course)
            
            visited.add(course)
            ans.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                # cycle detected
                return []
        return ans