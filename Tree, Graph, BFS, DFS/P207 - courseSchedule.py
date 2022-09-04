def dfs(course):
            if course in visited:
                return False
            if not adjList[course]:
                return True
            
            visited.add(course)
            for preReq in adjList[course]:
                if not dfs(preReq):
                    return False
            visited.remove(course)
            # Do this because, we do not need to again run DFS on same course
            adjList[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True